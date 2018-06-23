from Enumerations.cellPosition import CellPosition
from Enumerations.facet import Facet
from MagicCube.MagicCube import MagicCube
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

def getMagicCubeDict(magicCube:MagicCube):
    result=dict()
    for facet in Facet:
        cubefacet = magicCube[facet]
        facetDict = dict()
        for cellPosition in CellPosition:
            facetDict[str(cellPosition.name)] = {
                "value":str(cubefacet[cellPosition].value.name),
                "distance":cubefacet[cellPosition].distance()
            }
        result[str(facet)]=facetDict
    return result

@app.route("/position/")
@app.route("/position/<position_code>")
def show_position(position_code=None):
    if position_code is None or len(position_code) is not 54:
        mc = MagicCube()
    else:
        mc = MagicCube(position_code)
    mc.rotate(Facet.FRONT,True)
    position=getMagicCubeDict(mc)
    mcstr = str(mc)
    return render_template('main_template.html', mcstr = mcstr, position=position)

#
# if __name__ == '__main__':
# #     #app.run(debug=True)
#     mc = MagicCube()
#     getMagicCubeDict(mc)
