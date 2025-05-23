import minecraft_launcher_lib.utils

def get_filtered_versions(directory, include_snapshots=False):
    versions = minecraft_launcher_lib.utils.get_available_versions(directory)
    return [v['id'] for v in versions if v['type'] == 'release' or (include_snapshots and v['type'] == 'snapshot')]
