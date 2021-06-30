from PyQt5.QtCore import QVariant
from qgis._gui import QgsMapTool
from qgis._core import QgsFields, QgsField, QgsVectorFileWriter, QgsWkbTypes, QgsCoordinateReferenceSystem, QgsFeature, \
    QgsGeometry
from qgis.utils import iface

class PointTool(QgsMapTool):

    def __init__(self, canvas,context):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.i = 0
        self.list = []
        self.context = context

    def canvasPressEvent(self, event):
        pass

    def canvasMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)

    def canvasReleaseEvent(self, event):
        #Get the click
        x = event.pos().x()
        y = event.pos().y()
        print(x)
        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        self.savePoints(point)
        if self.i == 5 :
            self.createPolygone()
            self.i=0
            self.list.clear()

    def activate(self):
        pass

    def deactivate(self):
        pass

    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True
    def savePoints(self,point):
        self.list.append(point)
        self.i += 1
        return list
    def createPolygone(self):
        layerFields = QgsFields()
        layerFields.append(QgsField('ID', QVariant.Int))
        layerFields.append(QgsField('X', QVariant.Double))
        layerFields.append(QgsField('Y', QVariant.Double))
        # define the file path for the new shapefile and creat it
        derogation.counterPolygons = derogation.checkFilePoints(self.context, "points")
        fn = "C:/Users/ilyasse2.0/Desktop/points_derogation/points/point" + str(derogation.counterPolygons) + '.shp'
        writer = QgsVectorFileWriter(fn, 'UTF-8', layerFields, QgsWkbTypes.Polygon,
                                     QgsCoordinateReferenceSystem('EPSG:26191'), 'ESRI Shapefile')
        # First, create an empty QgsFeature().
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromPolygonXY([self.list]))
        i = 0
        while i < len(self.list) :
            feat.setAttributes([1, self.list[i][0], self.list[i][1]])
            writer.addFeature(feat)
            i += 1
        iface.addVectorLayer(fn, '', 'ogr')
        del (writer)
