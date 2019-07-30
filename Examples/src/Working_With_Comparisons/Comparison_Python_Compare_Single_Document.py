# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities

class Comparison_Python_Compare_Single_Document:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_CompareApi_Instance()
        
        try:
            options = groupdocs_comparison_cloud.Options()
            
            # Source file
            sourceFileInfo = groupdocs_comparison_cloud.FileInfo()
            sourceFileInfo.file_path = "Comparisondocs\\source_protected.docx"
            sourceFileInfo.password = "1231"
            sourceFileInfo.storage_name = Common_Utilities.myStorage
            
            options.source_file = sourceFileInfo    
            options.output_path = "Comparisondocs\\result_single_protected.docx"
            
            options.settings = groupdocs_comparison_cloud.Settings()
            options.settings.generate_summary_page = True
            options.settings.show_deleted_content = True
            options.settings.style_change_detection = True
            options.settings.use_frames_for_del_ins_elements = False
            options.settings.meta_data = None
            options.settings.detail_level = "Low"
            options.settings.diagram_master_setting = None
            options.settings.calculate_component_coordinates = False
            options.settings.clone_metadata = "Default"
            options.settings.mark_deleted_inserted_content_deep = False
            options.settings.password = "1111"
            options.settings.password_save_option = "User"
            
            options.settings.deleted_items_style = groupdocs_comparison_cloud.ItemsStyle()        
            options.settings.deleted_items_style.begin_separator_string = ""
            options.settings.deleted_items_style.end_separator_string = ""
            options.settings.deleted_items_style.font_color = "16711680"
            options.settings.deleted_items_style.highlight_color = "16711680"
            options.settings.deleted_items_style.bold = False
            options.settings.deleted_items_style.italic = False
            options.settings.deleted_items_style.strike_through = False
            
            options.settings.inserted_items_style = groupdocs_comparison_cloud.ItemsStyle()        
            options.settings.inserted_items_style.begin_separator_string = ""
            options.settings.inserted_items_style.end_separator_string = ""
            options.settings.inserted_items_style.font_color = "255"
            options.settings.inserted_items_style.highlight_color = "255"
            options.settings.inserted_items_style.bold = False
            options.settings.inserted_items_style.italic = False
            options.settings.inserted_items_style.strike_through = False
            
            options.settings.style_changed_items_style = groupdocs_comparison_cloud.ItemsStyle()
            options.settings.style_changed_items_style.begin_separator_string = ""
            options.settings.style_changed_items_style.end_separator_string = ""
            options.settings.style_changed_items_style.font_color = "65280"
            options.settings.style_changed_items_style.highlight_color = "65280"
            options.settings.style_changed_items_style.bold = False
            options.settings.style_changed_items_style.italic = False
            options.settings.style_changed_items_style.strike_through = False
            
            # Target file
            targetFileInfo = groupdocs_comparison_cloud.FileInfo()
            targetFileInfo.file_path = "Comparisondocs\\target_protected.docx"
            targetFileInfo.password = "5784"
            targetFileInfo.storage_name = Common_Utilities.myStorage
            
            options.target_files = [targetFileInfo]
            
            request = groupdocs_comparison_cloud.ComparisonsRequest(options)
            response = api.comparisons(request)
            
            print("Expected response type is Link: " + response.href)
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))