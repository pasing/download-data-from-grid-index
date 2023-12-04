import geopandas as gpd

def get_file_path_from_attribute(service_url, url_field_name):
    """
    # TODO Add documentation

    :param service_url:
    :param url_field_name:
    :return:
    """
    gdf = gpd.read_file(service_url)
    file_paths = gdf[url_field_name].tolist()
    return file_paths