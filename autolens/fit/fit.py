import numpy as np

from autoarray.fit import fit as aa_fit
from autoastro.galaxy import galaxy as g
from autolens.dataset import dataset as d


def fit(masked_dataset, tracer, hyper_image_sky=None, hyper_background_noise=None):

    if isinstance(masked_dataset, d.MaskedImaging):
        return ImagingFit(
            masked_imaging=masked_dataset,
            tracer=tracer,
            hyper_image_sky=hyper_image_sky,
            hyper_background_noise=hyper_background_noise,
        )
    elif isinstance(masked_dataset, d.MaskedInterferometer):
        return InterferometerFit(
            masked_interferometer=masked_dataset,
            tracer=tracer,
            hyper_background_noise=hyper_background_noise,
        )


class ImagingFit(aa_fit.ImagingFit):
    def __init__(
        self, masked_imaging, tracer, hyper_image_sky=None, hyper_background_noise=None
    ):
        """ An  lens fitter, which contains the tracer's used to perform the fit and functions to manipulate \
        the lens dataset's hyper_galaxies.

        Parameters
        -----------
        tracer : ray_tracing.Tracer
            The tracer, which describes the ray-tracing and strong lens configuration.
        scaled_array_2d_from_array_1d : func
            A function which maps the 1D lens hyper_galaxies to its unmasked 2D arrays.
        """

        self.masked_dataset = masked_imaging
        self.tracer = tracer

        image = hyper_image_from_image_and_hyper_image_sky(
            image=masked_imaging.image, hyper_image_sky=hyper_image_sky
        )

        noise_map = hyper_noise_map_from_noise_map_tracer_and_hyper_backkground_noise(
            noise_map=masked_imaging.noise_map,
            tracer=tracer,
            hyper_background_noise=hyper_background_noise,
        )

        self.blurred_profile_image = tracer.blurred_profile_image_from_grid_and_convolver(
            grid=masked_imaging.grid,
            convolver=masked_imaging.convolver,
            blurring_grid=masked_imaging.blurring_grid,
        )

        self.profile_subtracted_image = image - self.blurred_profile_image

        if not tracer.has_pixelization:

            inversion = None
            model_image = self.blurred_profile_image

        else:

            inversion = tracer.inversion_imaging_from_grid_and_data(
                grid=masked_imaging.grid,
                image=self.profile_subtracted_image,
                noise_map=noise_map,
                convolver=masked_imaging.convolver,
                inversion_uses_border=masked_imaging.inversion_uses_border,
                preload_sparse_grids_of_planes=masked_imaging.preload_sparse_grids_of_planes,
            )

            model_image = (
                self.blurred_profile_image + inversion.mapped_reconstructed_image
            )

        super().__init__(
            mask=masked_imaging.mask,
            image=image,
            noise_map=noise_map,
            model_image=model_image,
            inversion=inversion,
        )

    @property
    def grid(self):
        return self.masked_imaging.grid

    @property
    def galaxy_model_image_dict(self) -> {g.Galaxy: np.ndarray}:
        """
        A dictionary associating galaxies with their corresponding model images
        """
        galaxy_model_image_dict = self.tracer.galaxy_blurred_profile_image_dict_from_grid_and_convolver(
            grid=self.grid,
            convolver=self.masked_imaging.convolver,
            blurring_grid=self.masked_imaging.blurring_grid,
        )

        # TODO : Extend to multiple inversioons across Planes

        for plane_index in self.tracer.plane_indexes_with_pixelizations:

            galaxy_model_image_dict.update(
                {
                    self.tracer.planes[plane_index].galaxies[
                        0
                    ]: self.inversion.mapped_reconstructed_image
                }
            )

        return galaxy_model_image_dict

    @property
    def model_images_of_planes(self):

        model_images_of_planes = self.tracer.blurred_profile_images_of_planes_from_grid_and_psf(
            grid=self.grid,
            psf=self.masked_imaging.psf,
            blurring_grid=self.masked_imaging.blurring_grid,
        )

        for plane_index in self.tracer.plane_indexes_with_pixelizations:

            model_images_of_planes[
                plane_index
            ] += self.inversion.mapped_reconstructed_image

        return model_images_of_planes

    @property
    def unmasked_blurred_profile_image(self):
        return self.tracer.unmasked_blurred_profile_image_from_grid_and_psf(
            grid=self.grid, psf=self.masked_imaging.psf
        )

    @property
    def unmasked_blurred_profile_image_of_planes(self):
        return self.tracer.unmasked_blurred_profile_image_of_planes_from_grid_and_psf(
            grid=self.grid, psf=self.masked_imaging.psf
        )

    @property
    def unmasked_blurred_profile_image_of_planes_and_galaxies(self):
        return self.tracer.unmasked_blurred_profile_image_of_planes_and_galaxies_from_grid_and_psf(
            grid=self.grid, psf=self.masked_imaging.psf
        )

    @property
    def total_inversions(self):
        return len(list(filter(None, self.tracer.regularizations_of_planes)))


class InterferometerFit(aa_fit.InterferometerFit):
    def __init__(self, masked_interferometer, tracer, hyper_background_noise=None):
        """ An  lens fitter, which contains the tracer's used to perform the fit and functions to manipulate \
        the lens dataset's hyper_galaxies.

        Parameters
        -----------
        tracer : ray_tracing.Tracer
            The tracer, which describes the ray-tracing and strong lens configuration.
        scaled_array_2d_from_array_1d : func
            A function which maps the 1D lens hyper_galaxies to its unmasked 2D arrays.
        """

        if hyper_background_noise is not None:
            noise_map = hyper_background_noise.hyper_noise_map_from_noise_map(
                noise_map=masked_interferometer.noise_map
            )
        else:
            noise_map = masked_interferometer.noise_map

        self.masked_dataset = masked_interferometer
        self.tracer = tracer

        self.profile_visibilities = tracer.profile_visibilities_from_grid_and_transformer(
            grid=masked_interferometer.grid,
            transformer=masked_interferometer.transformer,
        )

        self.profile_subtracted_visibilities = (
            masked_interferometer.visibilities - self.profile_visibilities
        )

        if not tracer.has_pixelization:

            inversion = None
            model_visibilities = self.profile_visibilities

        else:

            inversion = tracer.inversion_interferometer_from_grid_and_data(
                grid=masked_interferometer.grid,
                visibilities=self.profile_subtracted_visibilities,
                noise_map=noise_map,
                transformer=masked_interferometer.transformer,
                inversion_uses_border=masked_interferometer.inversion_uses_border,
                preload_sparse_grids_of_planes=masked_interferometer.preload_sparse_grids_of_planes,
            )

            model_visibilities = (
                self.profile_visibilities + inversion.mapped_reconstructed_visibilities
            )

        super().__init__(
            visibilities_mask=masked_interferometer.visibilities_mask,
            visibilities=masked_interferometer.visibilities,
            noise_map=noise_map,
            model_visibilities=model_visibilities,
            inversion=inversion,
        )

    @property
    def grid(self):
        return self.masked_interferometer.grid

    @property
    def galaxy_model_image_dict(self) -> {g.Galaxy: np.ndarray}:
        """
        A dictionary associating galaxies with their corresponding model images
        """
        galaxy_model_image_dict = self.tracer.galaxy_profile_image_dict_from_grid(
            grid=self.grid
        )

        for path, image in galaxy_model_image_dict.items():
            if hasattr(image, "in_1d_binned"):
                galaxy_model_image_dict[path] = image.in_1d_binned

        # TODO : Extend to multiple inversioons across Planes

        for plane_index in self.tracer.plane_indexes_with_pixelizations:

            galaxy_model_image_dict.update(
                {
                    self.tracer.planes[plane_index].galaxies[
                        0
                    ]: self.inversion.mapped_reconstructed_image
                }
            )

        return galaxy_model_image_dict

    @property
    def galaxy_model_visibilities_dict(self) -> {g.Galaxy: np.ndarray}:
        """
        A dictionary associating galaxies with their corresponding model images
        """
        galaxy_model_visibilities_dict = self.tracer.galaxy_profile_visibilities_dict_from_grid_and_transformer(
            grid=self.masked_interferometer.grid,
            transformer=self.masked_interferometer.transformer,
        )

        # TODO : Extend to multiple inversioons across Planes

        for plane_index in self.tracer.plane_indexes_with_pixelizations:

            galaxy_model_visibilities_dict.update(
                {
                    self.tracer.planes[plane_index].galaxies[
                        0
                    ]: self.inversion.mapped_reconstructed_visibilities
                }
            )

        return galaxy_model_visibilities_dict

    def model_visibilities_of_planes(self):

        model_visibilities_of_planes = self.tracer.profile_visibilities_of_planes_from_grid_and_transformer(
            grid=self.masked_interferometer.grid,
            transformer=self.masked_interferometer.transformer,
        )

        for plane_index in self.tracer.plane_indexes_with_pixelizations:

            model_visibilities_of_planes[
                plane_index
            ] += self.inversion.mapped_reconstructed_image

        return model_visibilities_of_planes

    @property
    def total_inversions(self):
        return len(list(filter(None, self.tracer.regularizations_of_planes)))


class PositionsFit:
    def __init__(self, positions, tracer, noise_map):
        """A lens position fitter, which takes a set of positions (e.g. from a plane in the tracer) and computes \
        their maximum separation, such that points which tracer closer to one another have a higher likelihood.

        Parameters
        -----------
        positions : [[]]
            The (y,x) arc-second coordinates of positions which the maximum distance and likelihood is computed using.
        noise_map : ndarray | float
            The noise-value assumed when computing the likelihood.
        """
        self.positions = positions
        self.source_plane_positions = tracer.traced_grids_of_planes_from_grid(
            grid=positions
        )[-1]
        self.noise_map = noise_map

    def maximum_separation_within_threshold(self, threshold):
        return max(self.maximum_separations) <= threshold

    @property
    def maximum_separations(self):
        return [
            self.max_separation_of_grid(grid=position_list)
            for position_list in self.source_plane_positions.list_in_1d
        ]

    @staticmethod
    def max_separation_of_grid(grid):
        rdist_max = np.zeros((grid.sub_shape_1d))
        for i in range(grid.sub_shape_1d):
            xdists = np.square(np.subtract(grid[i, 0], grid[:, 0]))
            ydists = np.square(np.subtract(grid[i, 1], grid[:, 1]))
            rdist_max[i] = np.max(np.add(xdists, ydists))
        return np.max(np.sqrt(rdist_max))

    @property
    def chi_squared_map(self):
        return np.square(np.divide(self.maximum_separations, self.noise_map))

    @property
    def figure_of_merit(self):
        return -0.5 * sum(self.chi_squared_map)


def hyper_image_from_image_and_hyper_image_sky(image, hyper_image_sky):

    if hyper_image_sky is not None:
        return hyper_image_sky.hyper_image_from_image(image=image)
    else:
        return image


def hyper_noise_map_from_noise_map_tracer_and_hyper_backkground_noise(
    noise_map, tracer, hyper_background_noise
):

    hyper_noise_map = tracer.hyper_noise_map_from_noise_map(noise_map=noise_map)

    if hyper_background_noise is not None:
        noise_map = hyper_background_noise.hyper_noise_map_from_noise_map(
            noise_map=noise_map
        )

    if hyper_noise_map is not None:
        noise_map = noise_map + hyper_noise_map

    return noise_map
