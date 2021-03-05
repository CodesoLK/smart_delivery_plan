from flectra import fields, api, models, _


class NextDayDeliveryReportXls(models.AbstractModel):
    _name = 'report.smart_delivery_plan.report_next_day_delivery_xls'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, lines):
        # format1 = woorkbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        # format2 = woorkbook.add_format({'font_szie': 18, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Nexy Day Delivery Plan')
        # sheet.write(1,1, 'Next Day Delivery Plan', bold)
