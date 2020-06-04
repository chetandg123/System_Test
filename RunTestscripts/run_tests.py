
import sys
import os
import unittest
from HTMLTestRunner import HTMLTestRunner

from CRC import click_on_dashboad, select_crc_from_dashboard_menu, check_block_functionality, \
    check_block_wise_csv_download, check_cluster_functionality, check_cluster_wise_csv_download, \
    check_district_drop_down, check_district_functionality, check_district_wise_csv_download, \
    check_graph_and_table_on_home_page, check_home_button_functionality, check_logout_funtionality, \
    check_points_on_graph, check_school_wise_csv_download, check_table_contents, check_total_no_of_schools_in_crc, \
    check_total_no_of_students_in_crc, check_x_axis_dropdown, choose_x_axis_values, choose_y_axis_values, \
    click_on_select_type_option, select_block_wise
from Login import check_login_page, click_on_student_attendance_report, change_password, check_change_password, \
    click_on_back_button, click_on_create_user, click_on_dashboard, click_on_here_button, login_with_credencials, \
    login_with_invalid_credencials, login_with_invalid_user, login_without_credencials, setup_new_password, \
    test_on_change_password
from SAR import click_on_dashboard_menu, click_on_student_attendance, check_block_level_csv_download, \
    check_cluster_level_csv_download, check_logout, check_map_on_student_attendance_report, \
    check_navigation_functionality, check_no_of_schools_on_student_attendance_report, \
    check_no_of_students_on_student_attendance_report, check_points_on_map, check_school_dots_count, \
    check_student_attendance_tooltip_functionality, click_on_blocks, click_on_clusters, click_on_download, \
    click_on_home_button, click_on_schools, match_csv_file_with_api_call, mouse_over_on_blocks_dots, \
    mouse_over_on_cluster_dots, mouse_over_on_eash_dots, mouse_over_on_school_dots, selec_each_district_from_select_box, \
    select_district_block_cluster_and_click_on_csv, select_district_from_select_box, select_each_block_from_select_box, \
    select_each_cluster_from_select_box, select_month_wise_data
from Semester import click_on_semester, check_cluster_level_csv_downloads, check_logout_semester, check_map_on_semester, \
    check_navigation_functionality_for_semester, check_no_of_schools_on_semester, check_no_of_students_on_Semester, \
    check_points_on_semester_map, check_school_dots_count_on_semester, check_semester_tooltip_functionality, \
    click_on_dashboard_menu_of_semeter, check_block_level_csv_download_for_semester, click_on_semester_blocks, \
    click_on_semester_clusters, click_on_semester_download, click_on_semester_home_button, click_on_semester_schools, \
    match_csv_file_with_api_call_for_semester, mouse_over_on_blocks_dots_on_semester, \
    mouse_over_on_cluster_dots_on_semester, mouse_over_on_eash_dots_on_semester, mouse_over_on_school_dots_on_semester, \
    select_district_block_cluster_and_click_on_csv_in_semester, select_district_from_select_box_in_semester, \
    select_each_block_from_select_box_in_semester, select_each_cluster_from_select_box_in_semester, \
    select_each_district_from_select_box_in_semester


class MyTestSuite(unittest.TestCase):

    def test_issue1(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(check_login_page.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_credencials.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_student_attendance_report.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(change_password.ChangePassword),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_change_password.ChangePassword),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_back_button.OnRegularUser),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_create_user.UserCreate),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_dashboard.Dashboar),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_here_button.ClickHere),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_credencials.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_invalid_credencials.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_invalid_user.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_without_credencials.Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(setup_new_password.Password),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_on_change_password.Password),

            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_dashboard_menu.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_student_attendance.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_home_button.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_block_level_csv_download.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_cluster_level_csv_download.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_map_on_student_attendance_report.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_navigation_functionality.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_no_of_schools_on_student_attendance_report.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_no_of_students_on_student_attendance_report.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_points_on_map.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_school_dots_count.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_student_attendance_tooltip_functionality.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_blocks.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_clusters.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_download.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_home_button.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_schools.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(match_csv_file_with_api_call.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_blocks_dots.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_cluster_dots.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_eash_dots.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_school_dots.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(selec_each_district_from_select_box.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_district_block_cluster_and_click_on_csv.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_district_from_select_box.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_each_block_from_select_box.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_each_cluster_from_select_box.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_month_wise_data.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout.SAR),

            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_dashboad.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_crc_from_dashboard_menu.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_table_contents.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout_funtionality.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_block_functionality.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_block_wise_csv_download.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_cluster_functionality.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_cluster_wise_csv_download.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_district_drop_down.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_district_functionality.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_district_wise_csv_download.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_graph_and_table_on_home_page.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_home_button_functionality.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout_funtionality.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_points_on_graph.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_school_wise_csv_download.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_table_contents.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_total_no_of_schools_in_crc.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_total_no_of_students_in_crc.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_x_axis_dropdown.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(choose_x_axis_values.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(choose_y_axis_values.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_select_type_option.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_cluster_wise_csv_download.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_block_wise.CRC),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout_funtionality.CRC),


            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_dashboard_menu_of_semeter.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_map_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_block_level_csv_download_for_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_cluster_level_csv_downloads.Sem),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_blocks.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_map_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_home_button.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_navigation_functionality_for_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_no_of_schools_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_no_of_students_on_Semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_points_on_semester_map.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_school_dots_count_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_semester_tooltip_functionality.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_blocks.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_clusters.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_download.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_home_button.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_semester_schools.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(match_csv_file_with_api_call_for_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_blocks_dots_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_cluster_dots_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_eash_dots_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_school_dots_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(mouse_over_on_blocks_dots_on_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_district_block_cluster_and_click_on_csv_in_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_district_from_select_box_in_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_each_block_from_select_box_in_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_each_cluster_from_select_box_in_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(select_each_district_from_select_box_in_semester.Semester),
            unittest.defaultTestLoader.loadTestsFromTestCase(check_logout_semester.Semester)







        ])
        outfile = open('/home/devraj/PycharmProjects/RealeaseTests/SystemTest/Report/report.html', "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title ='Cqube System Test Report',
            verbosity = 1,

        )

        runner1.run(smoke_test)
        outfile.close()




if __name__ == '__main__':
    unittest.main()