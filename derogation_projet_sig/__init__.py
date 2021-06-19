# -*- coding: utf-8 -*-
"""
/***************************************************************************
 derogation
                                 A QGIS plugin
 projet_sig_derogation
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-06-19
        copyright            : (C) 2021 by GEOINFORMATION_BINOME_HANAFI_MOUSSA
        email                : ilyassehanafi@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load derogation class from file derogation.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .derogation_projet_sig import derogation
    return derogation(iface)
