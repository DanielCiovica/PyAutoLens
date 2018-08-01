import os
import shutil
from functools import wraps
from itertools import count

import pytest
from src.config import config
from src import exc
from src.autopipe import model_mapper
from src.autopipe import non_linear
from src.profiles import light_profiles, mass_profiles


@pytest.fixture(name='nlo_setup_path')
def test_nlo_setup():
    nlo_setup_path = "{}/../test_files/non_linear/nlo/setup/".format(os.path.dirname(os.path.realpath(__file__)))

    print(nlo_setup_path)

    if os.path.exists(nlo_setup_path):
        shutil.rmtree(nlo_setup_path)

    os.mkdir(nlo_setup_path)

    return nlo_setup_path


@pytest.fixture(name='nlo_paramnames_path')
def test_nlo_paramnames():
    nlo_paramnames_path = "{}/../test_files/non_linear/nlo/paramnames/".format(
        os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(nlo_paramnames_path):
        shutil.rmtree(nlo_paramnames_path)

    return nlo_paramnames_path


@pytest.fixture(name='nlo_model_info_path')
def test_nlo_model_info():
    nlo_model_info_path = "{}/../test_files/non_linear/nlo/model_info/".format(
        os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(nlo_model_info_path):
        shutil.rmtree(nlo_model_info_path)

    return nlo_model_info_path


@pytest.fixture(name='nlo_wrong_info_path')
def test_nlo_wrong_info():
    nlo_wrong_info_path = "{}/../test_files/non_linear/nlo/wrong_info/".format(
        os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(nlo_wrong_info_path):
        shutil.rmtree(nlo_wrong_info_path)

    os.mkdir(nlo_wrong_info_path)

    return nlo_wrong_info_path


@pytest.fixture(name='mn_summary_path')
def test_mn_summary():
    mn_summary_path = "{}/../test_files/non_linear/multinest/summary/".format(
        os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(mn_summary_path):
        shutil.rmtree(mn_summary_path)

    os.mkdir(mn_summary_path)

    return mn_summary_path


@pytest.fixture(name='mn_priors_path')
def test_mn_priors():
    mn_priors_path = "{}/../test_files/non_linear/multinest/priors/".format(os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(mn_priors_path):
        shutil.rmtree(mn_priors_path)

    os.mkdir(mn_priors_path)

    return mn_priors_path


@pytest.fixture(name='mn_samples_path')
def test_mn_samples():
    mn_samples_path = "{}/../test_files/non_linear/multinest/samples/".format(
        os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(mn_samples_path):
        shutil.rmtree(mn_samples_path)

    os.mkdir(mn_samples_path)

    return mn_samples_path


@pytest.fixture(name='config_path')
def test_config_path():
    return "{}/../test_files/config/priors/default/".format(os.path.dirname(os.path.realpath(__file__)))


def create_path(func):
    @wraps(func)
    def wrapper(path):
        if not os.path.exists(path):
            os.makedirs(path)
        return func(path)

    return wrapper


@create_path
def create_summary_4_parameters(path):
    summary = open(path + '/summary.txt', 'w')
    summary.write('    0.100000000000000000E+01   -0.200000000000000000E+01    0.300000000000000000E+01'
                  '    0.400000000000000000E+01   -0.500000000000000000E+01    0.600000000000000000E+01'
                  '    0.700000000000000000E+01    0.800000000000000000E+01'
                  '    0.900000000000000000E+01   -1.000000000000000000E+01   -1.100000000000000000E+01'
                  '    1.200000000000000000E+01    1.300000000000000000E+01   -1.400000000000000000E+01'
                  '   -1.500000000000000000E+01    1.600000000000000000E+01'
                  '    0.020000000000000000E+00    0.999999990000000000E+07'
                  '    0.020000000000000000E+00    0.999999990000000000E+07\n')
    summary.write('    0.100000000000000000E+01   -0.200000000000000000E+01    0.300000000000000000E+01'
                  '    0.400000000000000000E+01   -0.500000000000000000E+01    0.600000000000000000E+01'
                  '    0.700000000000000000E+01    0.800000000000000000E+01'
                  '    0.900000000000000000E+01   -1.000000000000000000E+01   -1.100000000000000000E+01'
                  '    1.200000000000000000E+01    1.300000000000000000E+01   -1.400000000000000000E+01'
                  '   -1.500000000000000000E+01    1.600000000000000000E+01'
                  '    0.020000000000000000E+00    0.999999990000000000E+07')
    summary.close()


@create_path
def create_summary_10_parameters(path):
    summary = open(path + '/summary.txt', 'w')
    summary.write('    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01'
                  '    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01'
                  '   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01'
                  '    1.000000000000000000E+01    1.100000000000000000E+01    1.200000000000000000E+01'
                  '    1.300000000000000000E+01    1.400000000000000000E+01    1.500000000000000000E+01'
                  '    1.600000000000000000E+01   -1.700000000000000000E+01   -1.800000000000000000E+01'
                  '    1.900000000000000000E+01    2.000000000000000000E+01    2.100000000000000000E+01'
                  '    2.200000000000000000E+01    2.300000000000000000E+01    2.400000000000000000E+01'
                  '    2.500000000000000000E+01   -2.600000000000000000E+01   -2.700000000000000000E+01'
                  '    2.800000000000000000E+01    2.900000000000000000E+01    3.000000000000000000E+01'
                  '    3.100000000000000000E+01    3.200000000000000000E+01    3.300000000000000000E+01'
                  '    3.400000000000000000E+01   -3.500000000000000000E+01   -3.600000000000000000E+01'
                  '    3.700000000000000000E+01   -3.800000000000000000E+01   -3.900000000000000000E+01'
                  '    4.000000000000000000E+01'
                  '    0.020000000000000000E+00    0.999999990000000000E+07'
                  '    0.020000000000000000E+00    0.999999990000000000E+07\n')
    summary.write('    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01'
                  '    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01'
                  '   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01'
                  '    1.000000000000000000E+01    1.100000000000000000E+01    1.200000000000000000E+01'
                  '    1.300000000000000000E+01    1.400000000000000000E+01    1.500000000000000000E+01'
                  '    1.600000000000000000E+01   -1.700000000000000000E+01   -1.800000000000000000E+01'
                  '    1.900000000000000000E+01    2.000000000000000000E+01    2.100000000000000000E+01'
                  '    2.200000000000000000E+01    2.300000000000000000E+01    2.400000000000000000E+01'
                  '    2.500000000000000000E+01   -2.600000000000000000E+01   -2.700000000000000000E+01'
                  '    2.800000000000000000E+01    2.900000000000000000E+01    3.000000000000000000E+01'
                  '    3.100000000000000000E+01    3.200000000000000000E+01    3.300000000000000000E+01'
                  '    3.400000000000000000E+01   -3.500000000000000000E+01   -3.600000000000000000E+01'
                  '    3.700000000000000000E+01   -3.800000000000000000E+01   -3.900000000000000000E+01'
                  '    4.000000000000000000E+01'
                  '   -1.900000000000000000E+01   -2.000000000000000000E+01')
    summary.close()


@create_path
def create_gaussian_prior_summary_4_parameters(path):
    summary = open(path + '/summary.txt', 'w')
    summary.write('    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01'
                  '    0.410000000000000000E+01    0.500000000000000000E+01    0.600000000000000000E+01'
                  '    0.700000000000000000E+01    0.800000000000000000E+01'
                  '    0.900000000000000000E+01    1.000000000000000000E+01    1.100000000000000000E+01'
                  '    1.200000000000000000E+01    1.300000000000000000E+01    1.400000000000000000E+01'
                  '    1.500000000000000000E+01    1.600000000000000000E+01'
                  '    0.020000000000000000E+00    0.999999990000000000E+07'
                  '    0.020000000000000000E+00    0.999999990000000000E+07\n')
    summary.write('    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01'
                  '    0.410000000000000000E+01    0.500000000000000000E+01    0.600000000000000000E+01'
                  '    0.700000000000000000E+01    0.800000000000000000E+01'
                  '    0.900000000000000000E+01    1.000000000000000000E+01    1.100000000000000000E+01'
                  '    1.200000000000000000E+01    1.300000000000000000E+01    1.400000000000000000E+01'
                  '    1.500000000000000000E+01    1.600000000000000000E+01'
                  '    0.020000000000000000E+00    0.999999990000000000E+07')
    summary.close()


@create_path
def create_weighted_samples_4_parameters(path):
    with open(path + '/multinest.txt', 'w+') as weighted_samples:
        weighted_samples.write(
            '    0.020000000000000000E+00    0.999999990000000000E+07    0.110000000000000000E+01    0.210000000000000000E+01    0.310000000000000000E+01    0.410000000000000000E+01\n'
            '    0.020000000000000000E+00    0.999999990000000000E+07    0.090000000000000000E+01    0.190000000000000000E+01    0.290000000000000000E+01    0.390000000000000000E+01\n'
            '    0.010000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.050000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.200000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n'
            '    0.300000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01')


@create_path
def create_weighted_samples_10_parameters(path):
    weighted_samples = open(path + '/multinest.txt', 'w')
    weighted_samples.write(
        '    0.020000000000000000E+00    0.999999990000000000E+07    0.110000000000000000E+01    0.210000000000000000E+01    0.310000000000000000E+01    0.410000000000000000E+01   -0.510000000000000000E+01   -0.610000000000000000E+01   -0.710000000000000000E+01   -0.810000000000000000E+01    0.910000000000000000E+01    1.010000000000000000E+01\n'
        '    0.020000000000000000E+00    0.999999990000000000E+07    0.090000000000000000E+01    0.190000000000000000E+01    0.290000000000000000E+01    0.390000000000000000E+01   -0.490000000000000000E+01   -0.590000000000000000E+01   -0.690000000000000000E+01   -0.790000000000000000E+01    0.890000000000000000E+01    0.990000000000000000E+01\n'
        '    0.010000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.050000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.200000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01\n'
        '    0.300000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01   -0.500000000000000000E+01   -0.600000000000000000E+01   -0.700000000000000000E+01   -0.800000000000000000E+01    0.900000000000000000E+01    1.000000000000000000E+01')
    weighted_samples.close()


class MockClassNLOx4(object):

    component_number = 0

    def __init__(self, one=1, two=2, three=3, four=4):
        self.one = one
        self.two = two
        self.three = three
        self.four = four

    @property
    def subscript(self):
        return 'a'

    @property
    def parameter_labels(self):
        return [r'x4p0', r'x4p1', r'x4p2', r'x4p3']


class MockClassNLOx6(object):

    component_number = 1

    def __init__(self, one=(1,2), two=(3,4), three=3, four=4):

        self.one = one
        self.two = two
        self.three = three
        self.four = four

    @property
    def subscript(self):
        return 'b'

    @property
    def parameter_labels(self):
        return [r'x6p0', r'x6p1', r'x6p2', r'x6p3', r'x6p4', r'x6p5']


class TestGenerateLatex(object):

    def test__one_parameter__no_subscript(self):
        assert non_linear.generate_parameter_latex('x') == ['$x$']

    def test__three_parameters__no_subscript(self):
        assert non_linear.generate_parameter_latex(['x', 'y', 'z']) == ['$x$', '$y$', '$z$']

    def test__one_parameter__subscript__no_number(self):
        assert non_linear.generate_parameter_latex(['x'], subscript='d') == [r'$x_{\mathrm{d}}$']

    def test__three_parameters__subscript__no_number(self):
        assert non_linear.generate_parameter_latex(['x', 'y', 'z'], subscript='d') == [r'$x_{\mathrm{d}}$',
                                                                                       r'$y_{\mathrm{d}}$',
                                                                                       r'$z_{\mathrm{d}}$']


class TestNonLinearOptimizer(object):

    class TestDirectorySetup(object):

        def test__1_class__correct_directory(self, config_path, nlo_setup_path):

            nlo = non_linear.NonLinearOptimizer(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=nlo_setup_path + '1_class', config_path=config_path)
            nlo.variable.add_classes(parallel=MockClassNLOx4)
            nlo.save_model_info()

            assert os.path.exists(nlo_setup_path + '1_class') == True

    class TestTotalParameters:

        def test__1_class__four_parameters(self, config_path, nlo_setup_path):
            nlo = non_linear.NonLinearOptimizer(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=nlo_setup_path + '1_class', config_path=config_path)
            nlo.variable.add_classes(class_1=MockClassNLOx4)

            assert nlo.variable.total_parameters == 4

        def test__2_classes__six_parameters(self, config_path, nlo_setup_path):
            nlo = non_linear.NonLinearOptimizer(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=nlo_setup_path + '2_classes', config_path=config_path)

            nlo.variable.add_classes(class_1=MockClassNLOx4, class_2=MockClassNLOx6)

            assert nlo.variable.total_parameters == 10

    class TestCreateParamNames(object):

        def test__1_class_and_parameter_set(self, config_path, nlo_paramnames_path):

            nlo = non_linear.NonLinearOptimizer(model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                                                path=nlo_paramnames_path, config_path=config_path)

            nlo.variable.add_classes(mock_class=MockClassNLOx4)
            nlo.save_model_info()

            paramnames_file = open(nlo_paramnames_path + '/multinest.paramnames')

            paramnames = paramnames_file.readlines()

            assert paramnames[0] == r'mock_class_one                          $x4p0_{\mathrm{a1}}$' + '\n'
            assert paramnames[1] == r'mock_class_two                          $x4p1_{\mathrm{a1}}$' + '\n'
            assert paramnames[2] == r'mock_class_three                        $x4p2_{\mathrm{a1}}$' + '\n'
            assert paramnames[3] == r'mock_class_four                         $x4p3_{\mathrm{a1}}$' + '\n'

        def test__2_classes__includes_a_tuple(self, config_path, nlo_paramnames_path):

            nlo = non_linear.NonLinearOptimizer(model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                                                path=nlo_paramnames_path, config_path=config_path)

            nlo.variable.add_classes(mock_class_1=MockClassNLOx4)
            nlo.variable.add_classes(mock_class_2=MockClassNLOx6)
            nlo.save_model_info()

            paramnames_file = open(nlo_paramnames_path + '/multinest.paramnames')

            paramnames = paramnames_file.readlines()

            assert paramnames[0] == r'mock_class_1_one                        $x4p0_{\mathrm{a1}}$' + '\n'
            assert paramnames[1] == r'mock_class_1_two                        $x4p1_{\mathrm{a1}}$' + '\n'
            assert paramnames[2] == r'mock_class_1_three                      $x4p2_{\mathrm{a1}}$' + '\n'
            assert paramnames[3] == r'mock_class_1_four                       $x4p3_{\mathrm{a1}}$' + '\n'
            assert paramnames[4] == r'mock_class_2_one_0                      $x6p0_{\mathrm{b2}}$' + '\n'
            assert paramnames[5] == r'mock_class_2_one_1                      $x6p1_{\mathrm{b2}}$' + '\n'
            assert paramnames[6] == r'mock_class_2_two_0                      $x6p2_{\mathrm{b2}}$' + '\n'
            assert paramnames[7] == r'mock_class_2_two_1                      $x6p3_{\mathrm{b2}}$' + '\n'
            assert paramnames[8] == r'mock_class_2_three                      $x6p4_{\mathrm{b2}}$' + '\n'
            assert paramnames[9] == r'mock_class_2_four                       $x6p5_{\mathrm{b2}}$' + '\n'

    class TestMakeModelInfo(object):

        def test__single_class__outputs_all_info(self, config_path, nlo_model_info_path):

            nlo = non_linear.NonLinearOptimizer(model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                                                path=nlo_model_info_path, config_path=config_path)

            nlo.variable.add_classes(mock_class=MockClassNLOx4)
            nlo.save_model_info()

            model_info_file = open(nlo_model_info_path + '/model.info')

            model_info = model_info_file.readlines()

            assert model_info[0] == r'MockClassNLOx4' + '\n'
            assert model_info[1] == r'' + '\n'
            assert model_info[2] == r'one: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[3] == r'two: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[4] == r'three: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[5] == r'four: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'

        def test__two_models_and_parameter_sets__output_all_info(self, config_path, nlo_model_info_path):

            nlo = non_linear.NonLinearOptimizer(model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                                                path=nlo_model_info_path, config_path=config_path)

            nlo.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)
            nlo.save_model_info()

            model_info_file = open(nlo_model_info_path + '/model.info')

            model_info = model_info_file.readlines()

            assert model_info[0] == r'MockClassNLOx4' + '\n'
            assert model_info[1] == r'' + '\n'
            assert model_info[2] == r'one: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[3] == r'two: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[4] == r'three: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[5] == r'four: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[6] == r'' + '\n'
            assert model_info[7] == r'MockClassNLOx6' + '\n'
            assert model_info[8] == r'' + '\n'
            assert model_info[9] == r'one_0: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[10] == r'one_1: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[11] == r'two_0: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[12] == r'two_1: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[13] == r'three: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
            assert model_info[14] == r'four: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'

    class TestWrongModelInfo(object):

        def test__single_model__prior_changed_from_input_model__raises_error(self, config_path, nlo_wrong_info_path):
            with open(nlo_wrong_info_path + '/model.info', 'w') as file: file.write('The model info is missing :(')

            with pytest.raises(exc.PriorException):
                nl = non_linear.NonLinearOptimizer(
                    model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)), path=nlo_wrong_info_path)
                nl.variable.add_classes(mass_profile=mass_profiles.SphericalNFW)
                nl.save_model_info()


class TestMultiNest(object):

    class TestReadFromSummary:

        def test__read_most_probable__1_class_4_params(self, config_path, mn_summary_path):
            create_summary_4_parameters(path=mn_summary_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '1_class')
            mn.variable.add_classes(mock_class=MockClassNLOx4)

            most_probable = mn.most_probable_from_summary()

            assert most_probable == [1.0, -2.0, 3.0, 4.0]

        def test__read_most_probable__2_classes_6_params(self, config_path, mn_summary_path):
            create_summary_10_parameters(path=mn_summary_path + '2_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '2_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            most_probable = mn.most_probable_from_summary()

            assert most_probable == [1.0, 2.0, 3.0, 4.0, -5.0, -6.0, -7.0, -8.0, 9.0, 10.0]

        def test__most_probable__setup_model_instance__1_class_4_params(self, config_path, mn_summary_path):
            create_summary_4_parameters(path=mn_summary_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '/1_class')
            mn.variable.add_classes(mock_class=MockClassNLOx4)

            most_probable = mn.most_probable_instance_from_summary()

            assert most_probable.mock_class.one == 1.0
            assert most_probable.mock_class.two == -2.0
            assert most_probable.mock_class.three == 3.0
            assert most_probable.mock_class.four == 4.0

        def test__most_probable__setup_model_instance__2_classes_6_params(self, config_path, mn_summary_path):
            create_summary_10_parameters(path=mn_summary_path + '2_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '2_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            most_probable = mn.most_probable_instance_from_summary()

            assert most_probable.mock_class_1.one == 1.0
            assert most_probable.mock_class_1.two == 2.0
            assert most_probable.mock_class_1.three == 3.0
            assert most_probable.mock_class_1.four == 4.0

            assert most_probable.mock_class_2.one == (-5.0, -6.0)
            assert most_probable.mock_class_2.two == (-7.0, -8.0)
            assert most_probable.mock_class_2.three == 9.0
            assert most_probable.mock_class_2.four == 10.0

        def test__read_most_likely__1_class_4_params(self, config_path, mn_summary_path):
            create_summary_4_parameters(path=mn_summary_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '1_class')
            mn.variable.add_classes(mock_class=MockClassNLOx4)

            most_likely = mn.most_likely_from_summary()

            assert most_likely == [9.0, -10.0, -11.0, 12.0]

        def test__read_most_likely__2_classes_6_params(self, config_path, mn_summary_path):
            create_summary_10_parameters(path=mn_summary_path + '2_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '2_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            most_likely = mn.most_likely_from_summary()

            assert most_likely == [21.0, 22.0, 23.0, 24.0, 25.0, -26.0, -27.0, 28.0, 29.0, 30.0]

        def test__most_likely__setup_model_instance__1_class_4_params(self, config_path, mn_summary_path):
            create_summary_4_parameters(path=mn_summary_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '1_class')
            mn.variable.add_classes(mock_class=MockClassNLOx4)

            most_likely = mn.most_likely_instance_from_summary()

            assert most_likely.mock_class.one == 9.0
            assert most_likely.mock_class.two == -10.0
            assert most_likely.mock_class.three == -11.0
            assert most_likely.mock_class.four == 12.0

        def test__most_likely__setup_model_instance__2_classes_6_params(self, config_path, mn_summary_path):
            create_summary_10_parameters(path=mn_summary_path + '2_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_summary_path + '2_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            most_likely = mn.most_likely_instance_from_summary()

            assert most_likely.mock_class_1.one == 21.0
            assert most_likely.mock_class_1.two == 22.0
            assert most_likely.mock_class_1.three == 23.0
            assert most_likely.mock_class_1.four == 24.0

            assert most_likely.mock_class_2.one == (25.0, -26.0)
            assert most_likely.mock_class_2.two == (-27.0, 28.0)
            assert most_likely.mock_class_2.three == 29.0
            assert most_likely.mock_class_2.four == 30.0

    class TestGaussianPriors(object):

        def test__1_class__gaussian_priors_at_3_sigma_confidence(self, config_path, mn_priors_path):
            create_gaussian_prior_summary_4_parameters(path=mn_priors_path)
            create_weighted_samples_4_parameters(path=mn_priors_path)

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_priors_path)

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            gaussian_priors = mn.gaussian_priors_at_sigma_limit(sigma_limit=3.0)

            assert gaussian_priors[0][0] == 1.0
            assert gaussian_priors[1][0] == 2.0
            assert gaussian_priors[2][0] == 3.0
            assert gaussian_priors[3][0] == 4.1

            assert gaussian_priors[0][1] == pytest.approx(0.12, 1e-2)
            assert gaussian_priors[1][1] == pytest.approx(0.12, 1e-2)
            assert gaussian_priors[2][1] == pytest.approx(0.12, 1e-2)
            assert gaussian_priors[3][1] == pytest.approx(0.22, 1e-2)

        def test__1_profile__gaussian_priors_at_1_sigma_confidence(self, config_path, mn_priors_path):
            create_gaussian_prior_summary_4_parameters(path=mn_priors_path)
            create_weighted_samples_4_parameters(path=mn_priors_path)

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_priors_path)

            mn.variable.add_classes(mock_class=MockClassNLOx4)
            gaussian_priors = mn.gaussian_priors_at_sigma_limit(sigma_limit=1.0)

            # Use sigmas directly as rouding errors come in otherwise
            lower_sigmas = mn.model_at_lower_sigma_limit(sigma_limit=1.0)

            assert gaussian_priors[0][0] == 1.0
            assert gaussian_priors[1][0] == 2.0
            assert gaussian_priors[2][0] == 3.0
            assert gaussian_priors[3][0] == 4.1

            assert gaussian_priors[0][1] == pytest.approx(1.0 - lower_sigmas[0], 5e-2)
            assert gaussian_priors[1][1] == pytest.approx(2.0 - lower_sigmas[1], 5e-2)
            assert gaussian_priors[2][1] == pytest.approx(3.0 - lower_sigmas[2], 5e-2)
            assert gaussian_priors[3][1] == pytest.approx(4.1 - lower_sigmas[3], 5e-2)

    class TestWeightedSamples(object):

        def test__1_class__1st_first_weighted_sample__model_weight_and_likelihood(self, config_path, mn_samples_path):
            create_weighted_samples_4_parameters(path=mn_samples_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_class')

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            model, weight, likelihood = mn.weighted_sample_model_from_weighted_samples(index=0)

            assert model == [1.1, 2.1, 3.1, 4.1]
            assert weight == 0.02
            assert likelihood == -0.5 * 9999999.9

        def test__1_class__5th_weighted_sample__model_weight_and_likelihood(self, config_path, mn_samples_path):
            create_weighted_samples_4_parameters(path=mn_samples_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_class')

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            model, weight, likelihood = mn.weighted_sample_model_from_weighted_samples(index=5)

            assert model == [1.0, 2.0, 3.0, 4.0]
            assert weight == 0.1
            assert likelihood == -0.5 * 9999999.9

        def test__2_classes__1st_weighted_sample__model_weight_and_likelihood(self, config_path, mn_samples_path):
            create_weighted_samples_10_parameters(path=mn_samples_path + '2_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '2_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            model, weight, likelihood = mn.weighted_sample_model_from_weighted_samples(index=0)

            assert model == [1.1, 2.1, 3.1, 4.1, -5.1, -6.1, -7.1, -8.1, 9.1, 10.1]
            assert weight == 0.02
            assert likelihood == -0.5 * 9999999.9

        def test__2_classes__5th_weighted_sample__model_weight_and_likelihood(self, config_path,
                                                                              mn_samples_path):
            create_weighted_samples_10_parameters(path=mn_samples_path + '1_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            model, weight, likelihood = mn.weighted_sample_model_from_weighted_samples(index=5)

            assert model == [1.0, 2.0, 3.0, 4.0, -5.0, -6.0, -7.0, -8.0, 9.0, 10.0]
            assert weight == 0.1
            assert likelihood == -0.5 * 9999999.9

        def test__1_class__1st_weighted_sample_model_instance__include_weight_and_likelihood(self, config_path,
                                                                                             mn_samples_path):
            create_weighted_samples_4_parameters(path=mn_samples_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_class')

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            weighted_sample_model, weight, likelihood = mn.weighted_sample_instance_from_weighted_samples(index=0)

            assert weight == 0.02
            assert likelihood == -0.5 * 9999999.9

            assert weighted_sample_model.mock_class.one == 1.1
            assert weighted_sample_model.mock_class.two == 2.1
            assert weighted_sample_model.mock_class.three == 3.1
            assert weighted_sample_model.mock_class.four == 4.1

        def test__1_class__5th_weighted_sample_model_instance__include_weight_and_likelihood(self, config_path,
                                                                                             mn_samples_path):
            create_weighted_samples_4_parameters(path=mn_samples_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_class')

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            weighted_sample_model, weight, likelihood = mn.weighted_sample_instance_from_weighted_samples(index=5)

            assert weight == 0.1
            assert likelihood == -0.5 * 9999999.9

            assert weighted_sample_model.mock_class.one == 1.0
            assert weighted_sample_model.mock_class.two == 2.0
            assert weighted_sample_model.mock_class.three == 3.0
            assert weighted_sample_model.mock_class.four == 4.0

        def test__2_classes__1st_weighted_sample_model_instance__include_weight_and_likelihood(self, config_path,
                                                                                               mn_samples_path):
            create_weighted_samples_10_parameters(path=mn_samples_path + '1_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            weighted_sample_model, weight, likelihood = mn.weighted_sample_instance_from_weighted_samples(index=0)

            assert weight == 0.02
            assert likelihood == -0.5 * 9999999.9

            assert weighted_sample_model.mock_class_1.one == 1.1
            assert weighted_sample_model.mock_class_1.two == 2.1
            assert weighted_sample_model.mock_class_1.three == 3.1
            assert weighted_sample_model.mock_class_1.four == 4.1

            assert weighted_sample_model.mock_class_2.one == (-5.1, -6.1)
            assert weighted_sample_model.mock_class_2.two == (-7.1, -8.1)
            assert weighted_sample_model.mock_class_2.three == 9.1
            assert weighted_sample_model.mock_class_2.four == 10.1

        def test__2_classes__5th_weighted_sample_model_instance__include_weight_and_likelihood(self, config_path,
                                                                                               mn_samples_path):
            create_weighted_samples_10_parameters(path=mn_samples_path + '1_classes')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_classes')

            mn.variable.add_classes(mock_class_1=MockClassNLOx4, mock_class_2=MockClassNLOx6)

            weighted_sample_model, weight, likelihood = mn.weighted_sample_instance_from_weighted_samples(index=5)

            assert weight == 0.1
            assert likelihood == -0.5 * 9999999.9

            assert weighted_sample_model.mock_class_1.one == 1.0
            assert weighted_sample_model.mock_class_1.two == 2.0
            assert weighted_sample_model.mock_class_1.three == 3.0
            assert weighted_sample_model.mock_class_1.four == 4.0

            assert weighted_sample_model.mock_class_2.one == (-5.0, -6.0)
            assert weighted_sample_model.mock_class_2.two == (-7.0, -8.0)
            assert weighted_sample_model.mock_class_2.three == 9.0
            assert weighted_sample_model.mock_class_2.four == 10.0

    class TestLimits(object):

        def test__1_profile__limits_1d_vectors_via_weighted_samples__1d_vectors_are_correct(self, config_path,
                                                                                            mn_samples_path):
            create_weighted_samples_4_parameters(path=mn_samples_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_class')

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            assert mn.model_at_upper_sigma_limit(sigma_limit=3.0) == pytest.approx([1.12, 2.12, 3.12, 4.12], 1e-2)
            assert mn.model_at_lower_sigma_limit(sigma_limit=3.0) == pytest.approx([0.88, 1.88, 2.88, 3.88], 1e-2)

        def test__1_profile__change_limit_to_1_sigma(self, config_path, mn_samples_path):
            create_weighted_samples_4_parameters(path=mn_samples_path + '1_class')

            mn = non_linear.MultiNest(
                model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
                path=mn_samples_path + '1_class')

            mn.variable.add_classes(mock_class=MockClassNLOx4)

            assert mn.model_at_upper_sigma_limit(sigma_limit=1.0) == pytest.approx([1.07, 2.07, 3.07, 4.07], 1e-2)
            assert mn.model_at_lower_sigma_limit(sigma_limit=1.0) == pytest.approx([0.93, 1.93, 2.93, 3.93], 1e-2)


class TestConfig(object):
    def test_multinest_default(self):
        multinest = non_linear.MultiNest()

        assert multinest.importance_nested_sampling is True

        assert multinest.multimodal is True
        assert multinest.const_efficiency_mode is False
        assert multinest.n_live_points == 400

        assert multinest.evidence_tolerance == 0.5
        assert multinest.sampling_efficiency == 0.8

        assert multinest.n_iter_before_update == 100
        assert multinest.null_log_evidence == -1e90

        assert multinest.max_modes == 100
        assert multinest.mode_tolerance == -1e90

        assert multinest.outputfiles_basename == "chains/1-"
        assert multinest.seed == -1
        assert multinest.verbose is False

        assert multinest.resume is True
        assert multinest.context == 0
        assert multinest.write_output is True
        assert multinest.log_zero == -1e100

        assert multinest.max_iter == 0
        assert multinest.init_MPI is False

    def test_downhill_simplex_default(self):
        downhill_simplex = non_linear.DownhillSimplex()

        assert downhill_simplex.xtol == 1e-4
        assert downhill_simplex.ftol == 1e-4
        assert downhill_simplex.maxiter is None
        assert downhill_simplex.maxfun is None

        assert downhill_simplex.full_output == 0
        assert downhill_simplex.disp == 1
        assert downhill_simplex.retall == 0


class TestRealClasses(object):

    def test__directory_setup__input_path_sets_up(self, config_path, nlo_setup_path):

        nlo = non_linear.NonLinearOptimizer(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=nlo_setup_path + '1_profile')

        nlo.variable.add_classes(light_profile=light_profiles.EllipticalSersic)
        nlo.save_model_info()

        assert os.path.exists(nlo_setup_path + '1_profile') == True

    def test__number_of_params__multiple_light_and_mass_profiles(self, config_path, nlo_setup_path):

        nlo = non_linear.NonLinearOptimizer(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=nlo_setup_path)

        nlo.variable.add_classes(light_profile=light_profiles.EllipticalSersic,
                                 light_profile_2=light_profiles.EllipticalSersic,
                                 light_profile_3=light_profiles.EllipticalSersic,
                                 mass_profile=mass_profiles.SphericalNFW,
                                 mass_profile_2=mass_profiles.SphericalNFW)

        assert nlo.variable.total_parameters == 29

    def test__create_param_names_2_light_models__2_mass_models(self, config_path, nlo_paramnames_path):

        light_profiles.EllipticalLightProfile._ids = count()
        mass_profiles.EllipticalMassProfile._ids = count()

        nlo = non_linear.NonLinearOptimizer(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=nlo_paramnames_path)

        nlo.variable.add_classes(
            light_profile_0=light_profiles.EllipticalSersic,
            light_profile_1=light_profiles.EllipticalExponential,
            mass_profile_0=mass_profiles.SphericalIsothermal,
            mass_profile_1=mass_profiles.SphericalNFW)

        nlo.save_model_info()

        paramnames_test = open(nlo_paramnames_path + 'multinest.paramnames')

        paramnames_str = paramnames_test.readlines()

        assert paramnames_str[0] == r'light_profile_0_centre_0                $x_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[1] == r'light_profile_0_centre_1                $y_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[2] == r'light_profile_0_axis_ratio              $q_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[3] == r'light_profile_0_phi                     $\phi_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[4] == r'light_profile_0_intensity               $I_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[5] == r'light_profile_0_effective_radius        $R_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[6] == r'light_profile_0_sersic_index            $n_{\mathrm{l1}}$' + '\n'
        assert paramnames_str[7] == r'light_profile_1_centre_0                $x_{\mathrm{l2}}$' + '\n'
        assert paramnames_str[8] == r'light_profile_1_centre_1                $y_{\mathrm{l2}}$' + '\n'
        assert paramnames_str[9] == r'light_profile_1_axis_ratio              $q_{\mathrm{l2}}$' + '\n'
        assert paramnames_str[10] == r'light_profile_1_phi                     $\phi_{\mathrm{l2}}$' + '\n'
        assert paramnames_str[11] == r'light_profile_1_intensity               $I_{\mathrm{l2}}$' + '\n'
        assert paramnames_str[12] == r'light_profile_1_effective_radius        $R_{\mathrm{l2}}$' + '\n'
        assert paramnames_str[13] == r'mass_profile_0_centre_0                 $x_{\mathrm{1}}$' + '\n'
        assert paramnames_str[14] == r'mass_profile_0_centre_1                 $y_{\mathrm{1}}$' + '\n'
        assert paramnames_str[15] == r'mass_profile_0_einstein_radius          $\theta_{\mathrm{1}}$' + '\n'
        assert paramnames_str[16] == r'mass_profile_1_centre_0                 $x_{\mathrm{d2}}$' + '\n'
        assert paramnames_str[17] == r'mass_profile_1_centre_1                 $y_{\mathrm{d2}}$' + '\n'
        assert paramnames_str[18] == r'mass_profile_1_kappa_s                  $\kappa_{\mathrm{d2}}$' + '\n'
        assert paramnames_str[19] == r'mass_profile_1_scale_radius             $Rs_{\mathrm{d2}}$' + '\n'

    def test__output_model_info__2_models(self, config_path, nlo_model_info_path):
        nlo = non_linear.NonLinearOptimizer(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=nlo_model_info_path)

        nlo.variable.add_classes(light_profile_0=light_profiles.EllipticalSersic,
                                 light_profile_1=light_profiles.EllipticalExponential,
                                 mass_profile_0=mass_profiles.SphericalIsothermal,
                                 mass_profile_1=mass_profiles.SphericalNFW)

        nlo.save_model_info()

        model_info_test = open(nlo_model_info_path + 'model.info')

        model_info_str = model_info_test.readlines()

        assert model_info_str[0] == r'EllipticalSersic' + '\n'
        assert model_info_str[1] == r'' + '\n'
        assert model_info_str[2] == r'centre_0: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
        assert model_info_str[3] == r'centre_1: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[4] == r'axis_ratio: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[5] == r'phi: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[6] == r'intensity: GaussianPrior, mean = 0.0, sigma = 0.5' + '\n'
        assert model_info_str[7] == r'effective_radius: UniformPrior, lower_limit = 1.0, upper_limit = 1.0' + '\n'
        assert model_info_str[8] == r'sersic_index: UniformPrior, lower_limit = 1.0, upper_limit = 1.0' + '\n'
        assert model_info_str[9] == r'' + '\n'
        assert model_info_str[10] == r'EllipticalExponential' + '\n'
        assert model_info_str[11] == r'' + '\n'
        assert model_info_str[12] == r'centre_0: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
        assert model_info_str[13] == r'centre_1: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[14] == r'axis_ratio: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[15] == r'phi: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[16] == r'intensity: GaussianPrior, mean = 0.0, sigma = 0.5' + '\n'
        assert model_info_str[17] == r'effective_radius: UniformPrior, lower_limit = 1.0, upper_limit = 1.0' + '\n'
        assert model_info_str[18] == r'' + '\n'
        assert model_info_str[19] == r'SphericalIsothermal' + '\n'
        assert model_info_str[20] == r'' + '\n'
        assert model_info_str[21] == r'centre_0: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
        assert model_info_str[22] == r'centre_1: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[23] == r'einstein_radius: UniformPrior, lower_limit = 1.0, upper_limit = 1.0' + '\n'
        assert model_info_str[24] == r'' + '\n'
        assert model_info_str[25] == r'SphericalNFW' + '\n'
        assert model_info_str[26] == r'' + '\n'
        assert model_info_str[27] == r'centre_0: UniformPrior, lower_limit = 0.0, upper_limit = 1.0' + '\n'
        assert model_info_str[28] == r'centre_1: UniformPrior, lower_limit = 0.0, upper_limit = 0.5' + '\n'
        assert model_info_str[29] == r'kappa_s: UniformPrior, lower_limit = 1.0, upper_limit = 1.0' + '\n'
        assert model_info_str[30] == r'scale_radius: UniformPrior, lower_limit = 1.0, upper_limit = 1.0' + '\n'

    def test__read_multinest_most_probable_via_summary__multiple_profiles(self, config_path, mn_summary_path):
        create_summary_10_parameters(path=mn_summary_path + 'multi_profile')

        files = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_summary_path + 'multi_profile')

        files.variable.add_classes(light_profile=light_profiles.EllipticalExponential,
                                   mass_profile=mass_profiles.SphericalNFW)

        files.save_model_info()

        most_probable = files.most_probable_from_summary()

        assert most_probable == [1.0, 2.0, 3.0, 4.0, -5.0, -6.0, -7.0, -8.0, 9.0, 10.0]

    def test__setup_most_probable_model_instance_via_multinest_summary(self, config_path, mn_summary_path):
        create_summary_10_parameters(path=mn_summary_path + 'multi_profile')

        files = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_summary_path + 'multi_profile')

        files.variable.add_classes(light_profile=light_profiles.EllipticalExponential,
                                   mass_profile=mass_profiles.SphericalNFW)

        files.save_model_info()

        most_likely = files.most_likely_from_summary()

        assert most_likely == [21.0, 22.0, 23.0, 24.0, 25.0, -26.0, -27.0, 28.0, 29.0, 30.0]

    def test__read_multinest_most_likely_via_summary__multiple_profiles(self, config_path, mn_summary_path):
        create_summary_10_parameters(path=mn_summary_path + 'multi_profile')

        files = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_summary_path + 'multi_profile')

        files.variable.add_classes(light_profile=light_profiles.EllipticalExponential,
                                   mass_profile=mass_profiles.SphericalNFW)

        files.save_model_info()

        max_likelihood = files.max_likelihood_from_summary()
        max_log_likelihood = files.max_log_likelihood_from_summary()

        assert max_likelihood == 0.02
        assert max_log_likelihood == 9999999.9

    def test__setup_most_likely_model_instance_via_multinest_summaryy(self, config_path, mn_summary_path):

        create_summary_10_parameters(path=mn_summary_path + 'multi_profile')

        multinest = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_summary_path + 'multi_profile')
        multinest.variable.add_classes(light_profile=light_profiles.EllipticalExponential,
                                       mass_profile=mass_profiles.SphericalNFW)

        multinest.save_model_info()

        most_probable = multinest.most_probable_instance_from_summary()
        most_likely = multinest.most_likely_instance_from_summary()

        assert most_probable.light_profile.centre == (1.0, 2.0)
        assert most_probable.light_profile.axis_ratio == 3.0
        assert most_probable.light_profile.phi == 4.0
        assert most_probable.light_profile.intensity == -5.0
        assert most_probable.light_profile.effective_radius == -6.0

        assert most_probable.mass_profile.centre == (-7.0, -8.0)
        assert most_probable.mass_profile.kappa_s == 9.0
        assert most_probable.mass_profile.scale_radius == 10.0

        assert most_likely.light_profile.centre == (21.0, 22.0)
        assert most_likely.light_profile.axis_ratio == 23.0
        assert most_likely.light_profile.phi == 24.0
        assert most_likely.light_profile.intensity == 25.0
        assert most_likely.light_profile.effective_radius == -26.0

        assert most_likely.mass_profile.centre == (-27.0, 28.0)
        assert most_likely.mass_profile.kappa_s == 29.0
        assert most_likely.mass_profile.scale_radius == 30.0

    def test__gaussian_priors_at_3_sigma_confidence__1_profile(self, config_path, mn_priors_path):
        create_gaussian_prior_summary_4_parameters(mn_priors_path)
        create_weighted_samples_4_parameters(mn_priors_path)

        results = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_priors_path)
        results.variable.add_classes(mass_profile=mass_profiles.SphericalNFW)

        results.save_model_info()

        gaussian_priors = results.gaussian_priors_at_sigma_limit(sigma_limit=3.0)

        assert gaussian_priors[0][0] == 1.0
        assert gaussian_priors[1][0] == 2.0
        assert gaussian_priors[2][0] == 3.0
        assert gaussian_priors[3][0] == 4.1

        assert gaussian_priors[0][1] == pytest.approx(0.12, 1e-2)
        assert gaussian_priors[1][1] == pytest.approx(0.12, 1e-2)
        assert gaussian_priors[2][1] == pytest.approx(0.12, 1e-2)
        assert gaussian_priors[3][1] == pytest.approx(0.22, 1e-2)

    def test__multiple_profiles__setup_fifth_weighted_sample_model__include_weight_and_likelihood(self, config_path,
                                                                                                  mn_samples_path):
        create_weighted_samples_10_parameters(mn_samples_path)

        nlo = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_samples_path)

        nlo.variable.light_profile = model_mapper.PriorModel(light_profiles.EllipticalExponential)
        nlo.variable.mass_profile = model_mapper.PriorModel(mass_profiles.SphericalNFW)

        nlo.save_model_info()

        weighted_sample_model, weight, likelihood = nlo.weighted_sample_instance_from_weighted_samples(index=5)

        assert weight == 0.1
        assert likelihood == -0.5 * 9999999.9

        assert weighted_sample_model.light_profile.centre == (1.0, 2.0)
        assert weighted_sample_model.light_profile.axis_ratio == 3.0
        assert weighted_sample_model.light_profile.phi == 4.0
        assert weighted_sample_model.light_profile.intensity == -5.0
        assert weighted_sample_model.light_profile.effective_radius == -6.0

        assert weighted_sample_model.mass_profile.centre == (-7.0, -8.0)
        assert weighted_sample_model.mass_profile.kappa_s == 9.0
        assert weighted_sample_model.mass_profile.scale_radius == 10.0

    def test__1_profile__limits_1d_vectors_via_weighted_samples__1d_vectors_are_correct(self, config_path,
                                                                                        mn_samples_path):
        create_weighted_samples_4_parameters(
            path=mn_samples_path)

        results = non_linear.MultiNest(
            model_mapper=model_mapper.ModelMapper(config=config.DefaultPriorConfig(config_path)),
            path=mn_samples_path)
        results.variable.add_class("mass_profile", mass_profiles.SphericalNFW)

        results.save_model_info()

        assert results.model_at_upper_sigma_limit(sigma_limit=3.0) == pytest.approx([1.12, 2.12, 3.12, 4.12],
                                                                                    1e-2)
        assert results.model_at_lower_sigma_limit(sigma_limit=3.0) == pytest.approx([0.88, 1.88, 2.88, 3.88],
                                                                                    1e-2)


class MockAnalysis(object):
    def __init__(self):
        self.kwargs = None

    def fit(self, **kwargs):
        self.kwargs = kwargs
        return 1.


@pytest.fixture(name='test_config')
def make_test_config():
    return config.DefaultPriorConfig(
        config_folder_path="{}/../{}".format(os.path.dirname(os.path.realpath(__file__)),
                                             "test_files/config/priors/default"))


@pytest.fixture(name="width_config")
def make_width_config():
    return config.WidthConfig(
        config_folder_path="{}/../{}".format(os.path.dirname(os.path.realpath(__file__)),
                                             "test_files/config/priors/width"))


@pytest.fixture(name="downhill_simplex")
def make_downhill_simplex(test_config, width_config):
    def fmin(fitness_function, x0):
        fitness_function(x0)
        return x0

    return non_linear.DownhillSimplex(fmin=fmin, model_mapper=model_mapper.ModelMapper(config=test_config,
                                                                                       width_config=width_config))


@pytest.fixture(name="multi_nest")
def make_multi_nest(test_config, width_config, mn_samples_path):
    create_weighted_samples_4_parameters(mn_samples_path)

    # noinspection PyUnusedLocal
    def run(fitness_function, prior, total_parameters, outputfiles_basename, n_clustering_params=None,
            wrapped_params=None, importance_nested_sampling=True, multimodal=True, const_efficiency_mode=False,
            n_live_points=400, evidence_tolerance=0.5, sampling_efficiency=0.8, n_iter_before_update=100,
            null_log_evidence=-1e+90, max_modes=100, mode_tolerance=-1e+90, seed=-1, verbose=False, resume=True,
            context=0,
            write_output=True, log_zero=-1e+100, max_iter=0, init_MPI=False, dump_callback=None):
        fitness_function([1 for _ in range(total_parameters)], total_parameters, total_parameters, None)

    create_summary_4_parameters(mn_samples_path)
    return non_linear.MultiNest(run=run, path=mn_samples_path,
                                model_mapper=model_mapper.ModelMapper(config=test_config, width_config=width_config))


class TestFitting(object):
    class TestDownhillSimplex(object):
        def test_constant(self, downhill_simplex):
            downhill_simplex.constant.mock_class = MockClassNLOx4()
            result = downhill_simplex.fit(MockAnalysis())

            assert result.constant.mock_class.one == 1
            assert result.constant.mock_class.two == 2
            assert result.likelihood == 1

        def test_variable(self, downhill_simplex, test_config):
            downhill_simplex.variable.mock_class = model_mapper.PriorModel(MockClassNLOx4, test_config)
            result = downhill_simplex.fit(MockAnalysis())

            assert result.constant.mock_class.one == 0.5
            assert result.constant.mock_class.two == 0.5
            assert result.likelihood == 1

            assert result.variable.mock_class.one.mean == 0.5
            assert result.variable.mock_class.two.mean == 0.5

        def test_constant_and_variable(self, downhill_simplex, test_config):
            downhill_simplex.constant.constant = MockClassNLOx4()
            downhill_simplex.variable.variable = model_mapper.PriorModel(MockClassNLOx4, test_config)

            result = downhill_simplex.fit(MockAnalysis())

            assert result.constant.constant.one == 1
            assert result.constant.constant.two == 2
            assert result.constant.variable.one == 0.5
            assert result.constant.variable.two == 0.5
            assert result.variable.variable.one.mean == 0.5
            assert result.variable.variable.two.mean == 0.5
            assert result.likelihood == 1

    class TestMultiNest(object):
        def test_variable(self, multi_nest, test_config):
            multi_nest.variable.mock_class = model_mapper.PriorModel(MockClassNLOx4, test_config)
            result = multi_nest.fit(MockAnalysis())

            assert result.constant.mock_class.one == 1
            assert result.constant.mock_class.two == 1
            assert result.likelihood == 1

            assert result.variable.mock_class.one.mean == 1
            assert result.variable.mock_class.two.mean == -2

        def test_constant_and_variable(self, multi_nest, test_config):

            multi_nest.constant.constant = MockClassNLOx4()
            multi_nest.variable.variable = model_mapper.PriorModel(MockClassNLOx4, test_config)

            result = multi_nest.fit(MockAnalysis())

            assert result.constant.constant.one == 1
            assert result.constant.constant.two == 2
            assert result.constant.variable.one == 1
            assert result.constant.variable.two == 1
            assert result.variable.variable.one.mean == 1
            assert result.variable.variable.two.mean == -2
            assert result.likelihood == 1