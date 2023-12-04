import os
import argparse

from urllib.parse import urlencode

from download_data_from_grid_index.downloader import download_file
from download_data_from_grid_index.utils import get_file_path_from_attribute

def main(args):
    """"""
    if args.base_url.endswith('/'):
        base_url = args.base_url[:-1]
    else:
        base_url = args.base_url
    workspace_name = args.workspace_name
    layer_name = f'{args.workspace_name}:{args.layer_name}'

    url_field_name = args.url_field_name
    output_directory = args.output_directory

    query_string = { 'service' : 'WFS', 'version' : '1.0.0', 'request' : 'GetFeature', 'typeName' : f'{layer_name}', 'outputFormat' : 'application/json'}
    service_url = f'{base_url}/{workspace_name}/ows?{urlencode(query_string)}'

    file_paths = get_file_path_from_attribute(service_url, url_field_name)

    for file_path in file_paths:
        file_name = file_path.split('/')[-1] # TODO Adjust this based on dynamic file structure
        os.makedirs(os.path.dirname(output_directory), exist_ok=True)
        output_file_path = os.path.join(output_directory, os.path.basename(file_name))
        download_file(file_path, output_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grid Index Features Data Downloader CLI")

    parser.add_argument('--base_url', default='http://sit.cittametropolitana.na.it/geoserver', help='Base URL of OGC Server')
    parser.add_argument('--workspace_name', default='sit', help='Workspace name')
    parser.add_argument('--layer_name', default='quadro_unione_lidar_dtm', help='Layer name')
    parser.add_argument('--url_field_name', default='url', help='URL field name')
    parser.add_argument('--output_directory', default='../data/dtm_asc/', help='Target directory for data')

    arguments = parser.parse_args()
    main(arguments)