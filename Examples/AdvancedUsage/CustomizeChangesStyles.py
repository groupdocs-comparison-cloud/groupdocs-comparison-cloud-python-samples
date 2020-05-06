# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to compare  documents with customizing changes styles
class CustomizeChangesStyles:
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
        settings.inserted_items_style = groupdocs_comparison_cloud.ItemsStyle()
        settings.inserted_items_style.highlight_color = "14297642"
        settings.inserted_items_style.font_color = "16711680"
        settings.inserted_items_style.underline = True
        settings.deleted_items_style = groupdocs_comparison_cloud.ItemsStyle()        
        settings.deleted_items_style.font_color = "14166746"
        settings.deleted_items_style.bold = True
        settings.changed_items_style = groupdocs_comparison_cloud.ItemsStyle()        
        settings.changed_items_style.font_color = "14320170"
        settings.changed_items_style.italic = True        
        options.settings = settings

        request = groupdocs_comparison_cloud.ComparisonsRequest(options)
        response = api_instance.comparisons(request)
        print("Output file link: " + response.href)