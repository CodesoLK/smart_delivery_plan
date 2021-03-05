from flectra import fields, api, models, _


class NextDayDeliveryReportXls(models.AbstractModel):
    _name = 'report.smart_delivery_plan.report_next_day_delivery_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        title_format = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        table_header_style = workbook.add_format({'font_size': 11, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Nexy Day Delivery Plan')
               
        # Column headers
        sheet.write(3,0, 'Priority Number', table_header_style)
        sheet.write(3,1, 'Order Date', table_header_style)
        sheet.write(3,2, 'Order Number', table_header_style)
        sheet.write(3,3, 'Product', table_header_style)
        sheet.write(3,4, 'Customer', table_header_style)
        sheet.write(3,5, 'Order QTY', table_header_style)
        sheet.write(3,6, 'Delivered QTY', table_header_style)
        sheet.write(3,7, 'To Delivered', table_header_style)
        sheet.write(3,8, 'Planing to Deliver', table_header_style)

        for line in lines:
            # Title of the report
            sheet.write_merge(1, 1, 1,10, 'Delivery Plan For ' + ' '+ line.delivery_date, title_format)
            
            if line.delivery_lines:
                row_number = 4
                for delivery_line in line.delivery_lines:
                    sheet.write(row_number, 0, '0', table_header_style)
                    sheet.write(row_number, 1, delivery_line.order_date, table_header_style)
                    sheet.write(row_number, 2, delivery_line.order_id.name, table_header_style)
                    sheet.write(row_number, 3, delivery_line.product_id.name, table_header_style)
                    sheet.write(row_number, 4, delivery_line.order_partner_id.name, table_header_style)
                    sheet.write(row_number, 5, delivery_line.product_uom_qty, table_header_style)
                    sheet.write(row_number, 6, delivery_line.qty_delivered, table_header_style)
                    sheet.write(row_number, 7, delivery_line.qty_delivery_available, table_header_style)
                    sheet.write(row_number, 8, delivery_line.plan_to_deliver, table_header_style)

                    row_number += 1
        
        
