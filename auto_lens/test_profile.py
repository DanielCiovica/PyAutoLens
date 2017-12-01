from __future__ import division, print_function

import numpy as np
import pytest
import profile

# noinspection PyClassHasNoInit
class TestEllipticalProfile:
    def test__coordinates_to_centre__mass_centre_zeros__no_shift(self):
        power_law = profile.EllipticalProfile(center=(0.0, 0.0), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == 0.0
        assert coordinates_shift[1] == 0.0

    def test__coordinates_to_centre__mass_centre_x_shift__x_shifts(self):
        power_law = profile.EllipticalProfile(center=(0.5, 0.0), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == -0.5
        assert coordinates_shift[1] == 0.0

    def test__coordinates_to_centre__mass_centre_y_shift__y_shifts(self):
        power_law = profile.EllipticalProfile(center=(0.0, 0.5), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == 0.0
        assert coordinates_shift[1] == -0.5

    def test__coordinates_to_centre__mass_centre_x_and_y_shift__x_and_y_both_shift(self):
        power_law = profile.EllipticalProfile(center=(0.5, 0.5), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == -0.5
        assert coordinates_shift[1] == -0.5

    def test__coordinates_to_centre__mass_centre_and_coordinates__correct_shifts(self):
        power_law = profile.EllipticalProfile(center=(1.0, 0.5), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.2, 0.4))

        assert coordinates_shift[0] == -0.8
        assert coordinates_shift[1] == pytest.approx(-0.1, 1e-5)

    def test__coordinates_to_radius__coordinates_overlap_mass_profile__r_is_zero(self):
        power_law = profile.EllipticalProfile(center=(0.0, 0.0), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0, 0))

        assert power_law.coordinates_to_radius(coordinates_shift) == 0.0

    def test__coordinates_to_radius__x_coordinates_is_one__r_is_one(self):
        power_law = profile.EllipticalProfile(center=(0.0, 0.0), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0))

        assert power_law.coordinates_to_radius(coordinates_shift) == 1.0

    def test__coordinates_to_radius__x_and_y_coordinates_are_one__r_is_root_two(self):
        power_law = profile.EllipticalProfile(center=(0.0, 0.0), axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.0))

        assert power_law.coordinates_to_radius(coordinates_shift) == pytest.approx(np.sqrt(2), 1e-5)

    def test__angles_from_x_axis__phi_is_zero__angles_one_and_zero(self):
        power_law = profile.EllipticalProfile(center=(1, 1), axis_ratio=1.0, phi=0.0)

        cos_phi, sin_phi = power_law.angles_from_x_axis()

        assert cos_phi == 1.0
        assert sin_phi == 0.0

    def test__angles_from_x_axis__phi_is_forty_five__angles_follow_trig(self):
        power_law = profile.EllipticalProfile(center=(1, 1), axis_ratio=1.0, phi=45.0)

        cos_phi, sin_phi = power_law.angles_from_x_axis()

        assert cos_phi == pytest.approx(0.707, 1e-3)
        assert sin_phi == pytest.approx(0.707, 1e-3)

    def test__angles_from_x_axis__phi_is_sixty__angles_follow_trig(self):
        power_law = profile.EllipticalProfile(center=(1, 1), axis_ratio=1.0, phi=60.0)

        cos_phi, sin_phi = power_law.angles_from_x_axis()

        assert cos_phi == pytest.approx(0.5, 1e-3)
        assert sin_phi == pytest.approx(0.866, 1e-3)

    def test__coordinates_angle_from_x__angle_is_zero__angles_follow_trig(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == 0.0

    def test__coordinates_angle_from_x__angle_is_forty_five__angles_follow_trig(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == 45.0

    def test__coordinates_angle_from_x__angle_is_sixty__angles_follow_trig(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.7320))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == pytest.approx(60.0, 1e-3)

    def test__coordinates_angle_from_x__top_left_quandrant__angle_goes_above_90(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(-1.0, 1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == 135.0

    def test__coordinates_angle_from_x__bottom_left_quandrant__angle_flips_back_to_45(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(-1.0, -1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == -135

    def test__coordinates_angle_from_x__bottom_right_quandrant__angle_flips_back_to_above_90(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, -1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == -45.0

    def test__coordinates_angle_to_mass_profile__same_angle__no_rotation(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        cos_theta, sin_theta = power_law.coordinates_angle_to_profile(theta_from_x)

        assert cos_theta == 1.0
        assert sin_theta == 0.0

    def test__coordinates_angle_to_mass_profile_both_45___no_rotation(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=45.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        cos_theta, sin_theta = power_law.coordinates_angle_to_profile(theta_from_x)

        assert cos_theta == pytest.approx(1.0, 1e-3)
        assert sin_theta == pytest.approx(0.0, 1e-3)

    def test__coordinates_angle_to_mass_profile_45_offset_same_angle__rotation_follows_trig(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        cos_theta, sin_theta = power_law.coordinates_angle_to_profile(theta_from_x)

        assert cos_theta == pytest.approx(0.707, 1e-3)
        assert sin_theta == pytest.approx(0.707, 1e-3)

    def test__coordinates_angle_to_mass_profile_negative_60_offset_same_angle__rotation_follows_trig(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=60.0)

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        cos_theta, sin_theta = power_law.coordinates_angle_to_profile(theta_from_x)

        assert cos_theta == pytest.approx(0.5, 1e-3)
        assert sin_theta == pytest.approx(-0.866, 1e-3)

    def test__coordinates_back_to_cartesian__phi_zero__no_rotation(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates_elliptical = (1.0, 1.0)

        x, y = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert x == 1.0
        assert y == 1.0

    def test__coordinates_back_to_cartesian__phi_ninety__correct_calc(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=90.0)

        coordinates_elliptical = (1.0, 1.0)

        x, y = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert x == pytest.approx(-1.0, 1e-3)
        assert y == 1.0

    def test__coordinates_back_to_cartesian__phi_forty_five__correct_calc(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=45.0)

        coordinates_elliptical = (1.0, 1.0)

        x, y = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert x == pytest.approx(0.0, 1e-3)
        assert y == pytest.approx(2 ** 0.5, 1e-3)

    def test__rotate_to_elliptical__phi_is_zero__returns_same_coordinates(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0)

        coordinates = (1.0, 1.0)

        x, y = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert x == pytest.approx(1.0, 1e-3)
        assert y == pytest.approx(1.0, 1e-3)

    def test__rotate_to_elliptical__phi_is_ninety__correct_rotation(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=90.0)

        # NOTE - whilst the profile and coordinates are defined counter-clockwise from x, the rotation is performed
        # clockwise

        coordinates = (1.0, 1.0)

        coordinates = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert coordinates[0] == pytest.approx(1.0, 1e-3)
        assert coordinates[1] == pytest.approx(-1.0, 1e-3)

    def test__rotate_to_elliptical__phi_is_one_eighty__correct_rotation(self):
        # NOTE - whilst the profile and coordinates are defined counter-clockwise from x, the rotation is performed
        # clockwise

        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=180.0)

        coordinates = (1.0, 1.0)

        coordinates = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert coordinates[0] == pytest.approx(-1.0, 1e-3)
        assert coordinates[1] == pytest.approx(-1.0, 1e-3)

    def test__rotate_to_elliptical__phi_is_two_seventy__correct_rotation(self):
        # NOTE - whilst the profile and coordinates are defined counter-clockwise from x, the rotation is performed
        # clockwise

        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=270.0)

        coordinates = (1.0, 1.0)

        coordinates = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert coordinates[0] == pytest.approx(-1.0, 1e-3)
        assert coordinates[1] == pytest.approx(1.0, 1e-3)

    def test__rotate_to_elliptical__phi_is_three_sixty__correct_rotation(self):
        # NOTE - whilst the profile and coordinates are defined counter-clockwise from x, the rotation is performed
        # clockwise

        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=360.0)

        coordinates = (1.0, 1.0)

        coordinates = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert coordinates[0] == pytest.approx(1.0, 1e-3)
        assert coordinates[1] == pytest.approx(1.0, 1e-3)

    def test__rotate_to_elliptical__phi_is_three_one_five__correct_rotation(self):
        # NOTE - whilst the profile and coordinates are defined counter-clockwise from x, the rotation is performed
        # clockwise

        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=315.0)

        coordinates = (1.0, 1.0)

        coordinates = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert coordinates[0] == pytest.approx(0.0, 1e-3)
        assert coordinates[1] == pytest.approx(2 ** 0.5, 1e-3)

    def test__rotate_to_elliptical__moving_lens_and_coordinates__same_answer(self):

        power_law1 = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0, center=(0,0))
        coordinates1 = (1.0, 1.0)
        coordinates1 = power_law1.coordinates_rotate_to_elliptical(coordinates1)

        power_law2 = profile.EllipticalProfile(axis_ratio=1.0, phi=0.0, center=(-1,-1))
        coordinates2 = (0.0, 0.0)
        coordinates2 = power_law2.coordinates_rotate_to_elliptical(coordinates2)

        assert coordinates1[0] == coordinates2[0]
        assert coordinates1[1] == coordinates2[1]

    def test__rotate_to_elliptical__moving_lens_and_coordinates_with_phi__same_answer(self):

        power_law1 = profile.EllipticalProfile(axis_ratio=1.0, phi=55.0, center=(0,0))
        coordinates1 = (1.0, 1.0)
        coordinates1 = power_law1.coordinates_rotate_to_elliptical(coordinates1)

        power_law2 = profile.EllipticalProfile(axis_ratio=1.0, phi=55.0, center=(-1,-1))
        coordinates2 = (0.0, 0.0)
        coordinates2 = power_law2.coordinates_rotate_to_elliptical(coordinates2)

        assert coordinates1[0] == coordinates2[0]
        assert coordinates1[1] == coordinates2[1]

    def test__rotate_to_elliptical__coordinates_both_on_center___same_answer(self):

        power_law1 = profile.EllipticalProfile(axis_ratio=1.0, phi=55.0, center=(1,1))
        coordinates1 = (1.0, 1.0)
        coordinates1 = power_law1.coordinates_rotate_to_elliptical(coordinates1)

        power_law2 = profile.EllipticalProfile(axis_ratio=1.0, phi=55.0, center=(-1,-1))
        coordinates2 = (-1.0, -1.0)
        coordinates2 = power_law2.coordinates_rotate_to_elliptical(coordinates2)

        assert coordinates1[0] == coordinates2[0]
        assert coordinates1[1] == coordinates2[1]

    def test_rotate_to_elliptical_coordinates_back_to_cartesian__are_consistent(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=315.0)

        coordinates_original = (5.2221, 2.6565)

        coordinates_elliptical = power_law.coordinates_rotate_to_elliptical(coordinates_original)

        coordinates = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert coordinates[0] == pytest.approx(coordinates_original[0], 1e-5)
        assert coordinates[1] == pytest.approx(coordinates_original[1], 1e-5)

    def test_rotate_to_elliptical_coordinates_back_to_cartesian_2__are_consistent(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=160.232)

        coordinates_original = (3.2, -76.6)

        coordinates_elliptical = power_law.coordinates_rotate_to_elliptical(coordinates_original)

        coordinates = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert coordinates[0] == pytest.approx(coordinates_original[0], 1e-2)
        assert coordinates[1] == pytest.approx(coordinates_original[1], 1e-2)

    def test_rotate_to_elliptical_coordinates_back_to_cartesian_3__are_consistent(self):
        power_law = profile.EllipticalProfile(axis_ratio=1.0, phi=174.342)

        coordinates_original = (-42.2, -93.6)

        coordinates_elliptical = power_law.coordinates_rotate_to_elliptical(coordinates_original)

        coordinates = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert coordinates[0] == pytest.approx(coordinates_original[0], 1e-2)
        assert coordinates[1] == pytest.approx(coordinates_original[1], 1e-2)


# noinspection PyClassHasNoInit
class TestSphericalProfile:
    def test__coordinates_to_centre__mass_centre_zeros__no_shift(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == 0.0
        assert coordinates_shift[1] == 0.0

    def test__coordinates_to_centre__mass_centre_x_shift__x_shifts(self):
        power_law = profile.SphericalProfile(center=(0.5, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == -0.5
        assert coordinates_shift[1] == 0.0

    def test__coordinates_to_centre__mass_centre_y_shift__y_shifts(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.5))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == 0.0
        assert coordinates_shift[1] == -0.5

    def test__coordinates_to_centre__mass_centre_x_and_y_shift__x_and_y_both_shift(self):
        power_law = profile.SphericalProfile(center=(0.5, 0.5))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.0, 0.0))

        assert coordinates_shift[0] == -0.5
        assert coordinates_shift[1] == -0.5

    def test__coordinates_to_centre__mass_centre_and_coordinates__correct_shifts(self):
        power_law = profile.SphericalProfile(center=(1.0, 0.5))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0.2, 0.4))

        assert coordinates_shift[0] == -0.8
        assert coordinates_shift[1] == pytest.approx(-0.1, 1e-5)

    def test__coordinates_to_radius__coordinates_overlap_mass_profile__r_is_zero(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(0, 0))

        assert power_law.coordinates_to_radius(coordinates_shift) == 0.0

    def test__coordinates_to_radius__x_coordinates_is_one__r_is_one(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0))

        assert power_law.coordinates_to_radius(coordinates_shift) == 1.0

    def test__coordinates_to_radius__x_and_y_coordinates_are_one__r_is_root_two(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.0))

        assert power_law.coordinates_to_radius(coordinates_shift) == pytest.approx(np.sqrt(2), 1e-5)

    def test__angles_from_x_axis__phi_is_zero__angles_one_and_zero(self):
        power_law = profile.SphericalProfile(center=(1, 1))

        cos_phi, sin_phi = power_law.angles_from_x_axis()

        assert cos_phi == 1.0
        assert sin_phi == 0.0

    def test__coordinates_angle_from_x__angle_is_zero__angles_follow_trig(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == 0.0

    def test__coordinates_angle_from_x__angle_is_forty_five__angles_follow_trig(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == 45.0

    def test__coordinates_angle_from_x__angle_is_sixty__angles_follow_trig(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 1.7320))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == pytest.approx(60.0, 1e-3)

    def test__coordinates_angle_from_x__top_left_quandrant__angle_goes_above_90(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(-1.0, 1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == 135.0

    def test__coordinates_angle_from_x__bottom_left_quandrant__angle_flips_back_to_45(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(-1.0, -1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == -135

    def test__coordinates_angle_from_x__bottom_right_quandrant__angle_flips_back_to_above_90(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, -1.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        assert theta_from_x == -45.0

    def test__coordinates_angle_to_mass_profile__same_angle__no_rotation(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_shift = power_law.coordinates_to_centre(shifted_coordinates=(1.0, 0.0))

        theta_from_x = power_law.coordinates_angle_from_x(coordinates_shift)

        cos_theta, sin_theta = power_law.coordinates_angle_to_profile(theta_from_x)

        assert cos_theta == 1.0
        assert sin_theta == 0.0

    def test__coordinates_back_to_cartesian__phi_zero__no_rotation(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_elliptical = (1.0, 1.0)

        x, y = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert x == 1.0
        assert y == 1.0

    def test__rotate_to_elliptical__phi_is_zero__returns_same_coordinates(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates = (1.0, 1.0)

        x, y = power_law.coordinates_rotate_to_elliptical(coordinates)

        assert x == pytest.approx(1.0, 1e-3)
        assert y == pytest.approx(1.0, 1e-3)

    def test_rotate_to_elliptical_coordinates_back_to_cartesian__are_consistent(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_original = (5.2221, 2.6565)

        coordinates_elliptical = power_law.coordinates_rotate_to_elliptical(coordinates_original)

        coordinates = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert coordinates[0] == pytest.approx(coordinates_original[0], 1e-5)
        assert coordinates[1] == pytest.approx(coordinates_original[1], 1e-5)

    def test_rotate_to_elliptical_coordinates_back_to_cartesian_2__are_consistent(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_original = (3.2, -76.6)

        coordinates_elliptical = power_law.coordinates_rotate_to_elliptical(coordinates_original)

        coordinates = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert coordinates[0] == pytest.approx(coordinates_original[0], 1e-2)
        assert coordinates[1] == pytest.approx(coordinates_original[1], 1e-2)

    def test_rotate_to_elliptical_coordinates_back_to_cartesian_3__are_consistent(self):
        power_law = profile.SphericalProfile(center=(0.0, 0.0))

        coordinates_original = (-42.2, -93.6)

        coordinates_elliptical = power_law.coordinates_rotate_to_elliptical(coordinates_original)

        coordinates = power_law.coordinates_back_to_cartesian(coordinates_elliptical)

        assert coordinates[0] == pytest.approx(coordinates_original[0], 1e-2)
        assert coordinates[1] == pytest.approx(coordinates_original[1], 1e-2)


# noinspection PyClassHasNoInit
class TestSersicLightProfile:
    def test__setup_sersic__correct_values(self):
        sersic = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                            effective_radius=0.6, sersic_index=4.0)

        assert sersic.x_cen == 0.0
        assert sersic.y_cen == 0.0
        assert sersic.axis_ratio == 1.0
        assert sersic.phi == 0.0
        assert sersic.flux == 1.0
        assert sersic.effective_radius == 0.6
        assert sersic.sersic_index == 4.0
        assert sersic.sersic_constant == pytest.approx(7.66925, 1e-3)

    def test__flux_at_radius__correct_value(self):
        sersic = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                            effective_radius=0.6, sersic_index=4.0)

        flux_at_radius = sersic.flux_at_radius(
            radius=1.0)  # 1.0 * exp(-7.66926 * (1.0/0.6) ** (1.0 / 4.0)) - 1) = 0.351797

        assert flux_at_radius == pytest.approx(0.351797, 1e-3)

    def test__flux_at_radius_2__correct_value(self):
        sersic = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=3.0,
                                            effective_radius=2.0, sersic_index=2.0)

        flux_at_radius = sersic.flux_at_radius(
            radius=1.5)  # 3.0 * exp(-3.67206544592 * (1,5/2.0) ** (1.0 / 2.0)) - 1) = 0.351797

        assert flux_at_radius == pytest.approx(4.90657319276, 1e-3)


# noinspection PyClassHasNoInit
class TestExponentialProfile:
    def test__setup_exponential__correct_values(self):
        sersic = profile.ExponentialLightProfile(center=(1, -1), axis_ratio=0.5, phi=45.0, flux=3.0,
                                                 effective_radius=0.2)

        assert sersic.x_cen == 1.0
        assert sersic.y_cen == -1.0
        assert sersic.axis_ratio == 0.5
        assert sersic.phi == 45.0
        assert sersic.flux == 3.0
        assert sersic.effective_radius == 0.2
        assert sersic.sersic_index == 1.0
        assert sersic.sersic_constant == pytest.approx(1.678378, 1e-3)


# noinspection PyClassHasNoInit
class TestDevVaucouleursProfile:
    def test__setup_dev_vaucouleurs__correct_values(self):
        sersic = profile.DevVaucouleursLightProfile(center=(0.0, 0.1), axis_ratio=0.6, phi=15.0, flux=2.0,
                                                    effective_radius=0.9)

        assert sersic.x_cen == 0.0
        assert sersic.y_cen == 0.1
        assert sersic.axis_ratio == 0.6
        assert sersic.phi == 15.0
        assert sersic.flux == 2.0
        assert sersic.effective_radius == 0.9
        assert sersic.sersic_index == 4.0
        assert sersic.sersic_constant == pytest.approx(7.66925, 1e-3)


# noinspection PyClassHasNoInit
class TestCoreSersicLightProfile:
    def test__core_sersic_light_profile(self):
        core_sersic = profile.CoreSersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                                     effective_radius=5, sersic_index=4.0, radius_break=0.01,
                                                     flux_break=0.1, gamma=1, alpha=1)
        # TODO: This seems way off? "flux_break = The intensity at the break radius."
        assert core_sersic.flux_at_radius(0.01) == 0.1


# noinspection PyClassHasNoInit
class TestEllipticalPowerLaw:
    def test__setup_elliptical_power_law__correct_values(self):
        power_law = profile.EllipticalPowerLawMassProfile(center=(1, 1), axis_ratio=1.0, phi=45.0,
                                                          einstein_radius=1.0
                                                          , slope=2.0)

        assert power_law.x_cen == 1.0
        assert power_law.y_cen == 1.0
        assert power_law.axis_ratio == 1.0
        assert power_law.phi == 45.0
        assert power_law.einstein_radius == 1.0
        assert power_law.slope == 2.0
        assert power_law.einstein_radius_rescaled == 0.5  # (3 - slope) / (1 + axis_ratio) = (3 - 2) / (1 + 1) = 0.5

# noinspection PyClassHasNoInit
class TestEllipticalIsotermal:
    def test__setup_elliptical_power_law__correct_values(self):
        power_law = profile.EllipticalIsothermalMassProfile(center=(1, 1), axis_ratio=1.0, phi=45.0,
                                                            einstein_radius=1.0)

        assert power_law.x_cen == 1.0
        assert power_law.y_cen == 1.0
        assert power_law.axis_ratio == 1.0
        assert power_law.phi == 45.0
        assert power_law.einstein_radius == 1.0
        assert power_law.slope == 2.0
        assert power_law.einstein_radius_rescaled == 0.5  # (3 - slope) / (1 + axis_ratio) = (3 - 2) / (1 + 1) = 0.5

    def test__compute_deflection_angle_no_coordinate_rotation__correct_values(self):

        isothermal = profile.EllipticalIsothermalMassProfile(center=(0, 0), axis_ratio=0.5, phi=0.0,
                                                            einstein_radius=1.0)

        defls = isothermal.compute_deflection_angle(coordinates=(1.0, 1.0))

       # normalization = (1/(1+q))*einr*q / (sqrt(1-q**2))
       # normalization = (1/1.5)*1*0.5 / (sqrt(0.75) = 0.3849
       # Psi = sqrt (q ** 2 * (x**2) + y**2 = 0.25 + 1) = sqrt(1.25)

       # defl_x = normalization * atan(sqrt(1-q**2) x / Psi )
       # defl_x = 0.3849 * atan(sqrt(0.75)/sqrt(1.25) = 0.25367

        # defl_y = normalization * atanh(sqrt(1-q**2) y / (Psi) )

        assert defls[0] == pytest.approx(0.25367, 1e-3)
        assert defls[1] == pytest.approx(0.397101,1e-3)

    def test__compute_deflection_angle_coordinate_rotation_90__defl_x_same_defl_y_flip(self):

        isothermal = profile.EllipticalIsothermalMassProfile(center=(0, 0), axis_ratio=0.5, phi=90.0,
                                                            einstein_radius=1.0)

        defls = isothermal.compute_deflection_angle(coordinates=(1.0, 1.0))

        assert defls[0] == pytest.approx(0.25367, 1e-3)
        assert defls[1] == pytest.approx(-0.397101,1e-3)

    def test__compute_deflection_angle_coordinate_rotation_180__both_defl_flip(self):

        isothermal = profile.EllipticalIsothermalMassProfile(center=(0, 0), axis_ratio=0.5, phi=180.0,
                                                            einstein_radius=1.0)

        defls = isothermal.compute_deflection_angle(coordinates=(1.0, 1.0))

        assert defls[0] == pytest.approx(-0.25367, 1e-3)
        assert defls[1] == pytest.approx(-0.397101,1e-3)

    def test__compute_deflection_angle_coordinate_rotation_45__defl_y_zero_new_defl_x(self):

        isothermal = profile.EllipticalIsothermalMassProfile(center=(0, 0), axis_ratio=0.5, phi=45.0,
                                                            einstein_radius=1.0)

        defls = isothermal.compute_deflection_angle(coordinates=(1.0, 1.0))

        # 45 degree aligns the mass profile with the axes, so there is no deflection acoss y.

        assert defls[0] == pytest.approx(0.40306, 1e-3)
        assert defls[1] == pytest.approx(0.0,1e-3)

    def test__compute_deflection_angle_double_einr__double_defl_angles(self):

        isothermal = profile.EllipticalIsothermalMassProfile(center=(0, 0), axis_ratio=0.5, phi=45.0,
                                                            einstein_radius=2.0)

        defls = isothermal.compute_deflection_angle(coordinates=(1.0, 1.0))

        assert defls[0] == pytest.approx(0.40306*2.0, 1e-3)
        assert defls[1] == pytest.approx(0.0,1e-3)

    def test__compute_deflection_angle_flip_coordinaates_and_centern__same_defl(self):

        isothermal = profile.EllipticalIsothermalMassProfile(center=(-1, -1), axis_ratio=0.5, phi=0.0,
                                                            einstein_radius=1.0)

        defls = isothermal.compute_deflection_angle(coordinates=(0.0, 0.0))

        assert defls[0] == pytest.approx(0.25367, 1e-3)
        assert defls[1] == pytest.approx(0.397101,1e-3)


@pytest.fixture(name='circular')
def circular_sersic():
    return profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                      effective_radius=0.6, sersic_index=4.0)


@pytest.fixture(name='elliptical')
def elliptical_sersic():
    return profile.SersicLightProfile(axis_ratio=0.5, phi=0.0, flux=1.0,
                                      effective_radius=0.6, sersic_index=4.0)


@pytest.fixture(name='vertical')
def vertical_sersic():
    return profile.SersicLightProfile(axis_ratio=0.5, phi=90.0, flux=1.0,
                                      effective_radius=0.6, sersic_index=4.0)


# noinspection PyClassHasNoInit
class TestArray:
    def test__simple_assumptions(self, circular):
        array = circular.as_array(x_min=0, x_max=101, y_min=0, y_max=101, pixel_scale=1)
        assert array.shape == (101, 101)
        assert array[51][51] > array[51][52]
        assert array[51][51] > array[52][51]
        assert all(map(lambda i: i > 0, array[0]))

        array = circular.as_array(x_min=0, x_max=100, y_min=0, y_max=100, pixel_scale=0.5)
        assert array.shape == (100, 100)

    def test__ellipticity(self, circular, elliptical, vertical):
        array = circular.as_array(x_min=0, x_max=101, y_min=0, y_max=101, pixel_scale=1)
        assert array[60][0] == array[0][60]

        array = elliptical.as_array(x_min=0, x_max=100, y_min=0, y_max=100, pixel_scale=1)

        assert array[60][51] > array[51][60]

        array = vertical.as_array(x_min=0, x_max=100, y_min=0, y_max=100, pixel_scale=1)
        assert array[60][51] < array[51][60]

    # noinspection PyTypeChecker
    def test__flat_array(self, circular):
        array = circular.as_array(x_min=0, x_max=100, y_min=0, y_max=100, pixel_scale=1)
        flat_array = circular.as_flat_array(x_min=0, x_max=100, y_min=0, y_max=100, pixel_scale=1)

        assert all(array[0] == flat_array[:100])
        assert all(array[1] == flat_array[100:200])

    def test_combined_array(self, circular):
        combined = profile.CombinedLightProfile(circular, circular)

        assert all(map(lambda i: i == 2, combined.as_flat_array() / circular.as_flat_array()))

    def test_symmetric_profile(self, circular):
        circular.center = (0, 0)
        array = circular.as_array(x_min=0, x_max=100, y_min=0, y_max=100, pixel_scale=1.0)

        assert array[50][50] > array[50][51]
        assert array[49][50] == array[50][51]
        assert array[50][51] == array[50][49]
        assert array[50][49] == array[51][50]


# noinspection PyClassHasNoInit
class TestCombinedProfiles:
    def test__summation(self, circular):
        combined = profile.CombinedLightProfile(circular, circular)
        assert combined.flux_at_coordinates((0, 0)) == 2 * circular.flux_at_coordinates((0, 0))

    def test_1d_symmetry(self):
        sersic1 = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                             effective_radius=0.6, sersic_index=4.0)

        sersic2 = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                             effective_radius=0.6, sersic_index=4.0, center=(100, 0))

        combined = profile.CombinedLightProfile(sersic1, sersic2)
        assert combined.flux_at_coordinates((0, 0)) == combined.flux_at_coordinates((100, 0))
        assert combined.flux_at_coordinates((49, 0)) == combined.flux_at_coordinates((51, 0))

    def test_2d_symmetry(self):
        sersic1 = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                             effective_radius=0.6, sersic_index=4.0)

        sersic2 = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                             effective_radius=0.6, sersic_index=4.0, center=(100, 0))
        sersic3 = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                             effective_radius=0.6, sersic_index=4.0, center=(0, 100))

        sersic4 = profile.SersicLightProfile(axis_ratio=1.0, phi=0.0, flux=1.0,
                                             effective_radius=0.6, sersic_index=4.0, center=(100, 100))

        combined = profile.CombinedLightProfile(sersic1, sersic2, sersic3, sersic4)

        assert combined.flux_at_coordinates((49, 0)) == pytest.approx(combined.flux_at_coordinates((51, 0)), 1e-5)
        assert combined.flux_at_coordinates((0, 49)) == pytest.approx(combined.flux_at_coordinates((0, 51)), 1e-5)
        assert combined.flux_at_coordinates((100, 49)) == pytest.approx(combined.flux_at_coordinates((100, 51)), 1e-5)
        assert combined.flux_at_coordinates((49, 49)) == pytest.approx(combined.flux_at_coordinates((51, 51)), 1e-5)
