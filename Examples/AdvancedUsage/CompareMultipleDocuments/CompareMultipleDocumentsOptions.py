# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to compare multiple documents with options
class CompareMultipleDocumentsOptions:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.CompareApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source.docx"
        target = groupdocs_comparison_cloud.FileInfo()
        target.file_path = "target_files/word/target.docx"  
        target1 = groupdocs_comparison_cloud.FileInfo()
        target1.file_path = "target_files/word/target_1.docx" 
        target2 = groupdocs_comparison_cloud.FileInfo()
        target2.file_path = "target_files/word/target_2.docx"                 
        options = groupdocs_comparison_cloud.ComparisonOptions()
        options.source_file = source
        options.target_files = [target, target1, target2] 
        options.output_path = "output/result.docx"
        settings = groupdocs_comparison_cloud.Settings()
        settings.inserted_items_style = groupdocs_comparison_cloud.ItemsStyle()
        settings.inserted_items_style.font_color = "16711680"
        options.settings = settings

        request = groupdocs_comparison_cloud.ComparisonsRequest(options)
        response = api_instance.comparisons(request)
        print("Output file link: " + response.href)