import unittest
from game.tests import test_Controller, test_GameViews, test_OXGame, test_OXModel


def run_tests():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(test_Controller))
    suite.addTests(loader.loadTestsFromModule(test_GameViews))
    suite.addTests(loader.loadTestsFromModule(test_OXGame))
    suite.addTests(loader.loadTestsFromModule(test_OXModel))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
