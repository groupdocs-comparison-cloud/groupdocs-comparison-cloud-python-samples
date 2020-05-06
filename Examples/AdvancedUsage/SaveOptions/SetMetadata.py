# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to set custom metadata for output document
class SetMetadata:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.CompareApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source.docx"
        target = groupdocs_comparison_cloud.FileInfo()
        target.file_path = "target_files/word/target.docx"          
        options = groupdocs_comparison_cloud.ComparisonOptions()
        options.source_file = source
        options.target_files = [target] 
        options.output_path = "output/result.docx"
        settings = groupdocs_comparison_cloud.Settings()
        settings.meta_data = groupdocs_comparison_cloud.Metadata()
        settings.meta_data.author = "Tom"
        settings.meta_data.company = "GroupDocs"
        settings.meta_data.last_save_by = "Jack"
        options.settings = settings

        request = groupdocs_comparison_cloud.ComparisonsRequest(options)
        response = api_instance.comparisons(request)
        print("Output file link: " + response.href)