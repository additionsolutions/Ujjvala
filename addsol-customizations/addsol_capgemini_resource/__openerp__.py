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
{
    'name' : 'Resource Management for Capgemini - Addsol',
    'version' : '1.0',
    'author' : 'Addition IT Solutions Pvt. Ltd.',
    'category' : 'Human Resource',
    'summary': 'Resource Management Customization for Capgemini',
    'description' : """
Resource Management for Capgemini
=================================
Contact:
--------
    * website: www.aitspl.com
    * email: info@aitspl.com    
    
Features:
---------
    * Project Manager can request for resources based on project needs.
    * Resource Manager can assign resources/approve/reject the request.
    * Resources can be searched based on their skills and can be selected automatically according to requirement criteria.
    * Project Manager can add tag(Soft Lock or Hard Lock) on request.
""",
    'depends' : ['addsol_resource','base_action_rule'],
    'data': [
        'addsol_capgemini_resource_view.xml',
        'report/addsol_capgemini_resource_reoprt_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
