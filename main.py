from flask import Flask, render_template, request, jsonify
import numpy as np
from decode import data
import matplotlib.pyplot as plt

app = Flask(__name__)

weights = np.array([-0.024956462776365873, 0.48290496052189424, -0.03870427179681009, -0.9975030460757535, 
           -0.2848756413600517, 0.6723778007493697, -3.273385514481454, 4.491796755394252,
           -0.12761211765843392, -0.80845330343299, -1.1575220884027035, -2.508206876120097, 
            -0.4197560564248292, -0.10480028817720448, -0.034035227772658674, 0.0, 3.1199435284876182,
           -0.6983902666978163, 0.40064004211711884, -0.14502170235576434, 0.06560835482410922, 0.1792180262947948])

bias = 0.8453068080484111

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def predict(x, w = weights, b = bias):
    p = np.dot(x, w) + b
    p = sigmoid(p)
    r = 0
    if p >= 0.5:
        r = 1
    return [p, r]

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/laboratory", methods=["GET", "POST"])
def lab():
    if request.method == "POST":
        # fetching data
        cap_shape = request.form["cap-shape"]
        cap_surface = request.form["cap-surface"]
        cap_color = request.form["cap-color"]
        bruises = request.form["bruises"]
        odor = request.form["odor"]
        gill_attachment = request.form["gill-attachment"]
        gill_spacing = request.form["gill-spacing"]
        gill_size = request.form["gill-size"]
        gill_color = request.form["gill-color"]
        stalk_shape = request.form["stalk-shape"]
        stalk_root = request.form["stalk-root"]
        stalk_surface_above_ring = request.form["stalk-surface-above-ring"]
        stalk_surface_below_ring = request.form["stalk-surface-below-ring"]
        stalk_color_above_ring = request.form["stalk-color-above-ring"]
        stalk_color_below_ring = request.form["stalk-color-below-ring"]
        veil_type = request.form["veil-type"]
        veil_color = request.form["veil-color"]
        ring_number = request.form["ring-number"]
        ring_type = request.form["ring-type"]
        spore_print_color = request.form["spore-print-color"]
        population = request.form["population"]
        habitat = request.form["habitat"]

        # processing data
        p_cap_shape = int(data["cap-shape"][cap_shape])
        p_cap_surface = int(data["cap-surface"][cap_surface])
        p_cap_color = int(data["cap-color"][cap_color])
        p_bruises = int(data["bruises"][bruises])
        p_odor = int(data["odor"][odor])
        p_gill_attachment = int(data["gill-attachment"][gill_attachment])
        p_gill_spacing = int(data["gill-spacing"][gill_spacing])
        p_gill_size = int(data["gill-size"][gill_size])
        p_gill_color = int(data["gill-color"][gill_color])
        p_stalk_shape = int(data["stalk-shape"][stalk_shape])
        p_stalk_root = int(data["stalk-root"][stalk_root])
        p_stalk_surface_above_ring = int(data["stalk-surface-above-ring"][stalk_surface_above_ring])
        p_stalk_surface_below_ring = int(data["stalk-surface-below-ring"][stalk_surface_below_ring])
        p_stalk_color_above_ring = int(data["stalk-color-above-ring"][stalk_color_above_ring])
        p_stalk_color_below_ring = int(data["stalk-color-below-ring"][stalk_color_below_ring])
        p_veil_type = int(data["veil-type"][veil_type])
        p_veil_color = int(data["veil-color"][veil_color])
        p_ring_number = int(data["ring-number"][ring_number])
        p_ring_type = int(data["ring-type"][ring_type])
        p_spore_print_color = int(data["spore-print-color"][spore_print_color])
        p_population = int(data["population"][population])
        p_habitat = int(data["habitat"][habitat])

        x = np.array([p_cap_shape, p_cap_surface, p_cap_color, p_bruises, p_odor, p_gill_attachment, p_gill_spacing, p_gill_size, p_gill_color, 
                      p_stalk_shape, p_stalk_root, p_stalk_surface_above_ring, p_stalk_surface_below_ring, p_stalk_color_above_ring, 
                      p_stalk_color_below_ring, p_veil_type, p_veil_color, p_ring_number, p_ring_type, p_spore_print_color, 
                      p_population, p_habitat])

        result = predict(x)[0]
        prediction = predict(x)[1]

        ## Plotting a Donut chart using matplotlib
        # sizes = [result, (1 - result)]
        # labels = ["Poisonous %", "Edible %"]
        # colors = ["#FF0000", "#0000FF"]
        # explosion = (0.05, 0.05)
        # plt.pie(sizes, colors = colors, labels = labels, autopct = "%1.1f%%", pctdistance=0.85, explode=explosion)
        # centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        # fig = plt.gcf()
        # fig.gca().add_artist(centre_circle)
        # plt.title("Mushroom Analysis")
        # plt.legend(labels, loc="upper right")
        # plt.show()
        
        processed_data = {
            "prediction": prediction,
            "Poisonous %": round(result * 100, 3),
            "edibility %": round((1 - result) * 100, 3),
            "Cap-shape" : cap_shape.capitalize(),
            "Cap-surface" : cap_surface.capitalize(),
            "Cap-color" : cap_color.capitalize(),
            "Bruises" : bruises.capitalize(),
            "Odor" : odor.capitalize(),
            "Gill-attachment" : gill_attachment.capitalize(),
            "Gill-spacing" : gill_spacing.capitalize(),
            "Gill-size" : gill_size.capitalize(),
            "Gill-color" : gill_color.capitalize(),
            "Stalk-shape" : stalk_shape.capitalize(),
            "Stalk-root" : stalk_root.capitalize(),
            "Stalk surface above ring" : stalk_surface_above_ring.capitalize(),
            "Stalk surface below ring" : stalk_surface_below_ring.capitalize(),
            "Stalk color above ring" : stalk_color_above_ring.capitalize(),
            "Stalk color below ring" : stalk_color_below_ring.capitalize(),
            "Veil-type" : veil_type.capitalize(),
            "Veil-color" : veil_color.capitalize(),
            "Rings-count" : ring_number.capitalize(),
            "Ring-type" : ring_type.capitalize(),
            "Spore-print color" : spore_print_color.capitalize(),
            "Population category" : population.capitalize(),
            "Habitat category" : habitat.capitalize(),
        }

        return render_template("results.html", api_data = processed_data)
    
    else:
        return render_template("form.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/api", methods=["GET"])
def chart():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)