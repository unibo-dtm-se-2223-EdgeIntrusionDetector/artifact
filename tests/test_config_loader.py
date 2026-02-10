import unittest
import tempfile
import os
import yaml

class TestConfigLoader(unittest.TestCase):
    """
    Test suite for the ConfigLoader class following TDD principles.
    """

    def setUp(self):
        """
        Prepares a temporary YAML configuration file before each test.
        """
        # Create a temporary file to simulate config.yaml
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.yaml')
        
        # Write some dummy data into it
        config_data = {
            'serial_port': '/dev/ttyUSB0',
            'baud_rate': 115200,
            'model_path': 'model.json'
        }
        yaml.dump(config_data, self.test_file)
        self.test_file.close()

    def tearDown(self):
        """
        Deletes the temporary file after each test.
        """
        os.unlink(self.test_file.name)

    def test_load_valid_config(self):
        """
        Test that a valid YAML file is loaded correctly.
        """
        # Import the class we haven't written yet (this will fail!)
        from edge_ids.config_loader import ConfigLoader

        # Create an instance (object) of the class
        loader = ConfigLoader()

        # Call the method to load the config from our temp file
        # self.test_file.name contains the path of the temporary file created in setUp
        config = loader.load_config(self.test_file.name)

        # Assertions: Check if the result is what we expect
        self.assertEqual(config['serial_port'], '/dev/ttyUSB0')
        self.assertEqual(config['baud_rate'], 115200)