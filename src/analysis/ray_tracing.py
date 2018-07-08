class Tracer(object):

    def __init__(self, lens_galaxies, source_galaxies, image_plane_grids):
        """The ray-tracing calculations, defined by a lensing system with just one image-plane and source-plane.

        This has no associated cosmology, thus all calculations are performed in arc seconds and galaxies do not need
        known redshift measurements. For computational efficiency, it is recommend this ray-tracing class is used for
        lens modeling, provided cosmological information is not necessary.

        Parameters
        ----------
        lens_galaxies : [Galaxy]
            The list of lens galaxies in the image-plane.
        source_galaxies : [Galaxy]
            The list of source galaxies in the source-plane.
        image_plane_grids : GridCoordsCollection
            The image-plane grids of coordinates where ray-tracing calculation are performed, (this includes the
            image.grid_coords, sub_grid, blurring.grid_coords etc.).
        """
        self.image_plane = Plane(lens_galaxies, image_plane_grids, compute_deflections=True)

        source_plane_grids = self.image_plane.trace_to_next_plane()

        self.source_plane = Plane(source_galaxies, source_plane_grids, compute_deflections=False)

    def generate_image_of_galaxy_light_profiles(self, mapping):
        """Generate the image of the galaxies over the entire ray trace."""
        return self.image_plane.generate_image_of_galaxy_light_profiles(mapping
        ) + self.source_plane.generate_image_of_galaxy_light_profiles(mapping)

    def generate_blurring_image_of_galaxy_light_profiles(self):
        """Generate the image of all galaxy light profiles in the blurring regions of the image."""
        if self.image_plane.grids.blurring is not None:
            return self.image_plane.generate_blurring_image_of_galaxy_light_profiles(
            ) + self.source_plane.generate_blurring_image_of_galaxy_light_profiles()


class Plane(object):

    def __init__(self, galaxies, grids, compute_deflections=True):
        """

        Represents a plane, which is a set of galaxies and grids at a given redshift in the lens ray-tracing
        calculation.

        The image-plane coordinates are defined on the observed image's uniform regular grid_coords. Calculating its
        model images from its light profiles exploits this uniformity to perform more efficient and precise calculations
        via an iterative sub-griding approach.

        The light profiles of galaxies at higher redshifts (and therefore in different lens-planes) can be assigned to
        the ImagePlane. This occurs when:

        1) The efficiency and precision offered by computing the light profile on a uniform grid_coords is preferred and
        won't lead noticeable inaccuracy. For example, computing the light profile of the main lens galaxy, ignoring
        minor lensing effects due to a low mass foreground substructure.

        2) When evaluating the light profile in its lens-plane is inaccurate. For example, when modeling the
        point-source images of a lensed quasar, effects like micro-lensing mean lens-plane modeling will be inaccurate.


        Parameters
        ----------
        galaxies : [Galaxy]
            The galaxies in the plane.
        grids : grids.GridCoordsCollection
            The grids of (x,y) coordinates in the plane, including the image grid_coords, sub-grid_coords, blurring,
            grid_coords, etc.
        """

        self.galaxies = galaxies
        self.grids = grids
        if compute_deflections:
            self.deflections = self.grids.deflection_grids_for_galaxies(self.galaxies)

    def trace_to_next_plane(self):
        """Trace the grids to the next plane.

        NOTE : This does not work for multi-plane lensing, which requires one to use the previous plane's deflection
        angles to perform the tracing. I guess we'll ultimately call this class 'LensPlanes' and have it as a list.
        """
        return self.grids.traced_grids_for_deflections(self.deflections)

    def generate_image_of_galaxy_light_profiles(self, mapping):
        """Generate the image of the galaxies in this plane."""
        return self.grids.sub.intensities_via_grid(self.galaxies, mapping)

    def generate_blurring_image_of_galaxy_light_profiles(self):
        """Generate the image of the galaxies in this plane."""
        return self.grids.blurring.intensities_via_grid(self.galaxies)

    def generate_pixelization_matrices_of_galaxy(self, mapping):
        for galaxy in self.galaxies:
            if galaxy.has_pixelization:
                   return galaxy.pixelization.compute_pixelization_matrices(self.grids.image, self.grids.blurring,
                                                                            mapping)
