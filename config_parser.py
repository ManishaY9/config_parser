import configparser
import json
import os
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

def parse_config_file(file_path='config.ini'):
    """
    Parse configuration file and extract key-value pairs.
    
    Args:
        file_path (str): Path to the configuration file.
    
    Returns:
        dict: Parsed configuration data
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Configuration file not found: {file_path}")
        
        # Initialize ConfigParser
        config = configparser.ConfigParser()
        config.read(file_path)
        
        # Parse configurations
        parsed_config = {}
        for section in config.sections():
            parsed_config[section] = dict(config[section])
        
        return parsed_config
    
    except Exception as e:
        return {"error": str(e)}

@app.route('/config', methods=['GET'])
def get_config():
    """
    API endpoint to retrieve the entire configuration.
    
    Returns:
        JSON response with configuration data
    """
    config_data = parse_config_file()
    if "error" in config_data:
        return jsonify(config_data), 500
    return jsonify(config_data)

@app.route('/config/<section>', methods=['GET'])
def get_config_section(section):
    """
    API endpoint to retrieve a specific section of the configuration.
    
    Args:
        section (str): Configuration section to retrieve.
    
    Returns:
        JSON response with the section data or an error message.
    """
    config_data = parse_config_file()
    if "error" in config_data:
        return jsonify(config_data), 500

    # Return the specific section or an error if not found
    section_data = config_data.get(section)
    if section_data:
        return jsonify(section_data)
    else:
        return jsonify({"error": f"Section '{section}' not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
