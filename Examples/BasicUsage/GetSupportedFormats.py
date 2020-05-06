# Import modules
import groupdocs_comparison_cloud
from Common import Common

#  This example demonstrates how to obtain all supported document formats
class GetSupportedFormats:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_comparison_cloud.InfoApi.from_config(Common.GetConfig())
        result = infoApi.get_supported_file_formats()
        print("Formats count: " + str(len(result.formats)))