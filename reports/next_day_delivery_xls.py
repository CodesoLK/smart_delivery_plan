from flectra import fields, api, models, _


class NextDayDeliveryReportXls(models.AbstractModel):
    _name = 'report.smart_delivery_plan.report_next_day_delivery_xls'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)