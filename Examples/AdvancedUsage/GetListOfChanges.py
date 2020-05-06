# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to get list of changes of compared documents
class GetListOfChanges:
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

        changes = api_instance.post_changes(groupdocs_comparison_cloud.PostChangesRequest(options))

        print("Changes count: " + str(len(changes)))