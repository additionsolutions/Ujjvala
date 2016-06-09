# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015-2016 Addition IT Solutions Pvt. Ltd. (<http://www.aitspl.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _

class resource_competancy(models.Model):
    _name = 'resource.competancy'
    _description = "Resource Competancy"

    name = fields.Char("Name", required=True)

class resource_skil_set(models.Model):
    _inherit = 'resource.skill.set'
    competancy_id = fields.Many2one('resource.competancy','Competancy',required=True)

class resource_request(models.Model):
    _inherit = 'resource.request'
    
    tag = fields.Selection([('soft_lock','Soft-Lock'),('hard_lock','Hard-Lock')], string="Tag")
    
class resource_request_lines(models.Model):
    _inherit = 'resource.request.lines'
    competancy_id = fields.Many2one('resource.competancy','Competancy',required=True)
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
