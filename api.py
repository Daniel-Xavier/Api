from sanic import Sanic
from sanic.response import text, json
from sanic_cors import CORS, cross_origin

app = Sanic(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def hello_world(request):
  return json({"msn": "Hello, cross-origin-world!"})

@app.route('/feeling', methods=['GET'])
async def get_feeling_handler(request):
    return json({
        'feeling': 'Joy',
    })


@app.route('/feeling/image', methods=['POST'])
async def post_image_handler(request):
    return await file(
        os.path.join(config.MOCK_DIR, 'face_predict_placeholder_1.jpg'),
        filename='img_predict.jpg'
    )

@app.route('/feeling/details' , methods=['GET'])
async def get_all_handler(request):
    return json({
        'feeling' : 'Joy',
        'action_units': ['AU6', 'AU13', 'AU17'],
        'model_used': 'Modelo_1',
        'accuracy': 0.9051,
        'avg_predict_time': 1051
    })

@app.route('/models' , methods=['GET'])
async def get_model_handler(request):
    return json({

        'models': [
        {'modelo_1': 'nome_modelo1',
         'accuracy': 0.9997,
         'avg_predict_time': 1234
        },
        {'modelo_2': 'nome_modelo2',
         'accuracy': 0.9449,
         'avg_predict_time': 1235
        },
        {'modelo_3': 'nome_modelo3',
         'accuracy': 0.6924,
         'avg_predict_time': 5244
        }]
    })

if __name__ == '__main__':
    app.run(debug=True)
