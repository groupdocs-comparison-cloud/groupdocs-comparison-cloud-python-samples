# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to accept/reject changes after documents compare
class AcceptOrRejectChanges:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.CompareApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source.docx"
        target = groupdocs_comparison_cloud.FileInfo()
        target.file_path = "target_files/word/target.docx"  
        options = groupdocs_comparison_cloud.UpdatesOptions()
        options.source_file = source
        options.target_files = [target] 
        options.output_path = "output/result.docx"

        changes = api_instance.post_changes(groupdocs_comparison_cloud.PostChangesRequest(options))

        for change in changes:
            change.comparison_action = "Reject"
        changes[0].comparison_action = "Accept"

        options.changes = changes

        response = api_instance.put_changes_document(groupdocs_comparison_cloud.PutChangesDocumentRequest(options))

        print("Output file link: " + response.href)