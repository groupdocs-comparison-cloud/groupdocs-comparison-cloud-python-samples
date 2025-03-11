# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to preview document
class PreviewDocument:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.PreviewApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source.docx"
        options = groupdocs_comparison_cloud.PreviewOptions()
        options.file_info = source
        options.format = "jpg" 
        options.output_folder = "output"

        request = groupdocs_comparison_cloud.PreviewRequest(options)
        response = api_instance.preview(request)
        print("Output file count: " + str(len(response)))
