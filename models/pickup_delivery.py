import datetime
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT

# ==========================================================================================================================

class pickup_delivery_trip(models.Model):
    _name = "pickup.delivery.trip"
    _description = "Modul for pickup and delivery trip system"

    name = 
    courier_id = fields.Many2one('hr.employee','Courier', ondelete='restrict')
    vehicle_id = fields.Many2many('fleet.vehicle','Vehicle', ondelete='restrict')
    departure_date = fields.Datetime('Departure Date')
    finished_date = fields.Datetime('Finished Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('on_the_way', 'On The Way'),
        ('finished', 'Finished'),
        ('cancelled', 'Cancelled'),
    ], 'State', required=True, default='draft')
    trip_line_ids = fields.One2many('pickup.delivery.trip.line','trip_id','Trip Lines')

    action_ready
    action_on_the_way
    action_finished
    action_cancelled

# ==========================================================================================================================

class pickup_delivery_trip_line(models.Model):
    _name = "pickup.delivery.trip.line"
    _description = "Line for every pickup and delivery trip"

    trip_id = fields.Many2one('pickup.delivery.trip','Trip', ondelete='cascade')
    request_id = fields.Many2one('pickup.delivery.request','Request',ondelete='cascade',domain=[('state','=','ready'),('state','=','delayed')])
    request_desc = 
    address = 
    delivery_type = fields.Selection([
        ('employee','Employee'),
        ('outsource','Outsource'),
    ], 'Delivery Type', required=True, default='employee')
    expedition_id = 
    notes = fields.Text('Notes')
    execute_status = fields.Selection([
        ('execute','Execute'),
        ('not_execute', 'Not Execute'),
    ],'Execute Status',required=True,default='default_value')
    partner_pic = fields.Char('PIC')