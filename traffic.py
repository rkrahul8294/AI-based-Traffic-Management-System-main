import os
import requests
from flask import Flask, jsonify, render_template, request, redirect, url_for, send_file

current_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=current_dir)

TOMTOM_KEY = "X3iHYfQxY30Mydgqb4GeJugDuK0RBxAs"

# ── LOGIN ──────────────────────────────────────────────────────────────────────

@app.route("/")
def start():
    return redirect(url_for('login'))

@app.route('/college_img')
def college_img():
    path = r"C:\Users\Rahul\Desktop\W46dJfdsnq.jpg"
    if os.path.exists(path):
        return send_file(path, mimetype='image/jpeg')
    return "Not found", 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123':
            return redirect(url_for('home'))
        else:
            return "<h3 style='color:#ef4444;font-family:sans-serif;padding:20px;text-align:center;margin-top:50px;'>Invalid Credentials! <a href='/login' style='color:#3b82f6'>Try Again</a></h3>"

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Traffic Admin Login</title>
        <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
                font-family: "Rajdhani", sans-serif;
                display: flex; flex-direction: column;
                align-items: center; justify-content: center;
                height: 100vh; color: #f1f5f9; overflow: hidden;
                background: url('/college_img') center center / cover no-repeat;
            }
            .bg-overlay { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.4); z-index: 1; }
            .lane-lines { position: fixed; inset: 0; z-index: 1; display: flex; justify-content: center; overflow: hidden; opacity: 0.6; }
            .lane-strip {
                width: 6px;
                background: repeating-linear-gradient(180deg, rgba(255,255,255,0.8) 0px, rgba(255,255,255,0.8) 40px, transparent 40px, transparent 80px);
                animation: roadMove 0.9s linear infinite;
            }
            @keyframes roadMove { 0% { background-position: 0 0; } 100% { background-position: 0 80px; } }
            .car-lane { position: fixed; inset: 0; z-index: 2; pointer-events: none; }
            .car { position: absolute; width: 4px; height: 18px; border-radius: 2px; animation: carMove linear infinite; }
            @keyframes carMove {
                0%   { top: -20px; opacity: 0; }
                5%   { opacity: 1; }
                95%  { opacity: 1; }
                100% { top: 110vh; opacity: 0; }
            }
            .glow-overlay {
                position: fixed; inset: 0; z-index: 3;
                background:
                    radial-gradient(ellipse 60% 50% at 30% 50%, rgba(37, 99, 235, 0.15) 0%, transparent 60%),
                    radial-gradient(ellipse 50% 60% at 70% 50%, rgba(6, 182, 212, 0.15) 0%, transparent 60%),
                    radial-gradient(ellipse 100% 40% at 50% 100%, rgba(15, 23, 42, 0.5) 0%, transparent 50%);
            }
            .grid-overlay {
                position: fixed; inset: 0; z-index: 4; opacity: 0.03;
                background-image: linear-gradient(rgba(255,255,255,1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,1) 1px, transparent 1px);
                background-size: 60px 60px;
            }
            .login-wrap { position: relative; z-index: 10; display: flex; flex-direction: column; align-items: center; gap: 16px; margin-top: 18vh; }
            .login-box {
                width: 340px; padding: 32px 28px;
                background: rgba(15, 23, 42, 0.3);
                backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 20px; text-align: center;
                box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
            }
            .logo-ring {
                width: 60px; height: 60px; margin: 0 auto 14px;
                border-radius: 50%;
                background: linear-gradient(135deg, #0ea5e9, #2563eb);
                border: 2px solid rgba(14, 165, 233, 0.3);
                display: flex; align-items: center; justify-content: center;
                font-size: 26px; box-shadow: 0 0 25px rgba(37, 99, 235, 0.4);
            }
            h2 { font-size: 19px; font-weight: 700; letter-spacing: 2.2px; color: #fff; margin-bottom: 4px; text-transform: uppercase; background: linear-gradient(90deg, #fff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .subtitle { font-size: 10px; color: rgba(148, 163, 184, 0.8); font-family: "JetBrains Mono", monospace; letter-spacing: 1.5px; margin-bottom: 22px; }
            .field-label { text-align: left; font-size: 9px; font-family: "JetBrains Mono", monospace; letter-spacing: 2px; color: rgba(241, 245, 249, 0.5); text-transform: uppercase; margin-bottom: 5px; margin-top: 12px; }
            input {
                width: 100%; padding: 10px 14px;
                background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(255,255,255,0.15);
                border-radius: 12px; color: white;
                font-family: "JetBrains Mono", monospace; font-size: 13px;
                outline: none; transition: border-color 0.3s, box-shadow 0.3s, background 0.3s;
                box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.2);
            }
            input:focus { border-color: rgba(59, 130, 246, 0.8); background: rgba(0, 0, 0, 0.5); box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.3), 0 0 0 2px rgba(59, 130, 246, 0.2); }
            input::placeholder { color: rgba(241, 245, 249, 0.3); }
            button {
                width: 100%; padding: 12px;
                background: linear-gradient(135deg, #2563eb, #1d4ed8);
                color: white; border: none;
                border-radius: 10px; cursor: pointer;
                font-family: "Rajdhani", sans-serif; font-size: 15px; font-weight: 700;
                letter-spacing: 2.5px; text-transform: uppercase;
                transition: all 0.3s; margin-top: 18px;
                box-shadow: 0 5px 15px rgba(37, 99, 235, 0.3);
            }
            button:hover { background: linear-gradient(135deg, #3b82f6, #2563eb); box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5); transform: translateY(-2px); }
            .divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent); margin: 20px 0 0 0; }
            .status-bar { display: flex; background: rgba(15, 23, 42, 0.3); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.1); border-radius: 50px; overflow: hidden; font-size: 11px; font-family: "JetBrains Mono", monospace; }
            .status-item { padding: 7px 18px; color: rgba(255,255,255,0.45); display: flex; align-items: center; gap: 6px; border-right: 1px solid rgba(255,255,255,0.07); }
            .status-item:last-child { border-right: none; }
            .dot { width: 6px; height: 6px; border-radius: 50%; background: #00e676; box-shadow: 0 0 6px #00e676; animation: dotPulse 2s ease-in-out infinite; }
            @keyframes dotPulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
        </style>
    </head>
    <body>
        <div class="bg-overlay"></div>
        <div class="lane-lines">
            <div class="lane-strip" style="margin:0 120px"></div>
            <div class="lane-strip" style="margin:0 60px;animation-delay:-0.3s"></div>
            <div class="lane-strip" style="animation-delay:-0.6s"></div>
            <div class="lane-strip" style="margin:0 -60px;animation-delay:-0.1s"></div>
            <div class="lane-strip" style="margin:0 -120px;animation-delay:-0.5s"></div>
        </div>
        <div class="car-lane" id="cars"></div>
        <div class="glow-overlay"></div>
        <div class="grid-overlay"></div>

        <div class="login-wrap">
            <div class="login-box">
                <div class="logo-ring">🚦</div>
                <h2>Smart Traffic System</h2>
                <p class="subtitle">ADMIN CONTROL PORTAL &middot; DEHRADUN</p>
                <form method="post">
                    <div class="field-label">Username</div>
                    <input type="text" name="username" placeholder="Enter admin username" required autocomplete="off">
                    <div class="field-label">Password</div>
                    <input type="password" name="password" placeholder="Enter password" required>
                    <button type="submit">Login to System</button>
                </form>
                <div class="divider"></div>
            </div>
            <div class="status-bar">
                <div class="status-item"><div class="dot"></div> SYSTEM ONLINE</div>
                <div class="status-item">📷 SENSORS ACTIVE</div>
                <div class="status-item">🖥️ NODE 01</div>
            </div>
        </div>

        <script>
            const lane = document.getElementById('cars');
            const colors = ['#3b82f6','#0ea5e9','#ffffff','#60a5fa','#38bdf8','#2dd4bf'];
            for (let i = 0; i < 20; i++) {
                const car = document.createElement('div');
                car.className = 'car';
                const offsetX = (Math.random() - 0.5) * window.innerWidth;
                const dur = (1.8 + Math.random() * 2.5).toFixed(2);
                const delay = -(Math.random() * 4).toFixed(2);
                const color = colors[Math.floor(Math.random() * colors.length)];
                car.style.cssText = `left:calc(50% + ${offsetX}px);animation-duration:${dur}s;animation-delay:${delay}s;background:${color};box-shadow:0 0 10px ${color},0 0 25px ${color}88;width:${3+Math.random()*2}px;height:${12+Math.random()*8}px`;
                lane.appendChild(car);
            }
        </script>
    </body>
    </html>
    '''


# ── DASHBOARD ─────────────────────────────────────────────────────────────────

@app.route("/dashboard")
def home():
    return render_template("index.html")


# ── ADAPTIVE TIMING LOGIC ─────────────────────────────────────────────────────

def calculate_adaptive_timings(speed):
    yellow = 5
    if speed < 15:
        green, red, status = 60, 20, "HEAVY JAM"
    elif speed < 30:
        green, red, status = 45, 30, "MODERATE"
    else:
        green, red, status = 35, 45, "CLEAR"
    return {"green": green, "yellow": yellow, "red": red, "status": status}


# ── TRAFFIC DATA API ──────────────────────────────────────────────────────────

@app.route("/traffic-data")
def get_traffic():
    locations = [
        {"name": "Clock Tower",    "lat": 30.3256, "lon": 78.0437},
        {"name": "ISBT Dehradun",  "lat": 30.2887, "lon": 78.0110},
        {"name": "Rajpur Road",    "lat": 30.3530, "lon": 78.0700},
        {"name": "Rispana Bridge", "lat": 30.2942, "lon": 78.0487},
        {"name": "Ballupur Chowk", "lat": 30.3145, "lon": 78.0167},
    ]
    results = []
    for loc in locations:
        try:
            url = (
                f"https://api.tomtom.com/traffic/services/4/flowSegmentData/"
                f"absolute/10/json?key={TOMTOM_KEY}&point={loc['lat']},{loc['lon']}"
            )
            res = requests.get(url, timeout=4).json()
            if "flowSegmentData" in res:
                fsd      = res["flowSegmentData"]
                speed    = fsd.get("currentSpeed", 0)
                freeflow = fsd.get("freeFlowSpeed", speed)
                congestion = round((1 - speed / max(freeflow, 1)) * 100, 1) if freeflow > 0 else 0
                t = calculate_adaptive_timings(speed)
                results.append({
                    **loc, "speed": speed,
                    "freeFlowSpeed": freeflow,
                    "congestion": congestion,
                    "traffic": t["status"],
                    "timings": {"green": t["green"], "yellow": t["yellow"], "red": t["red"]}
                })
            else:
                raise ValueError("missing flowSegmentData")
        except Exception as e:
            print(f"[WARN] {loc['name']}: {e}")
            results.append({
                **loc, "speed": 20, "freeFlowSpeed": 40, "congestion": 50,
                "traffic": "MODERATE",
                "timings": {"green": 35, "yellow": 5, "red": 25}
            })
    return jsonify(results)


# ── ROUTE TRAFFIC CHECK API ───────────────────────────────────────────────────

@app.route("/route-traffic-check", methods=["POST"])
def route_traffic_check():
    """
    POST body: { "points": [{lat, lon}, ...], "routeIdx": 0|1|2 }
    Returns heavy jams on route + alternate route suggestion.
    """
    import math

    data        = request.get_json(force=True)
    route_points = data.get("points", [])
    route_idx   = data.get("routeIdx", 0)

    locations = [
        {"name": "Clock Tower",    "lat": 30.3256, "lon": 78.0437},
        {"name": "ISBT Dehradun",  "lat": 30.2887, "lon": 78.0110},
        {"name": "Rajpur Road",    "lat": 30.3530, "lon": 78.0700},
        {"name": "Rispana Bridge", "lat": 30.2942, "lon": 78.0487},
        {"name": "Ballupur Chowk", "lat": 30.3145, "lon": 78.0167},
    ]

    def haversine(lat1, lon1, lat2, lon2):
        R = 6371
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = math.sin(dLat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2)**2
        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    jams_on_route = []
    for loc in locations:
        on_route = any(
            haversine(p["lat"], p["lon"], loc["lat"], loc["lon"]) < 2.5
            for p in route_points
        )
        if not on_route:
            continue
        try:
            url = (
                f"https://api.tomtom.com/traffic/services/4/flowSegmentData/"
                f"absolute/10/json?key={TOMTOM_KEY}&point={loc['lat']},{loc['lon']}"
            )
            res      = requests.get(url, timeout=4).json()
            fsd      = res.get("flowSegmentData", {})
            speed    = fsd.get("currentSpeed", 20)
            freeflow = fsd.get("freeFlowSpeed", 40)
        except:
            speed, freeflow = 20, 40

        t = calculate_adaptive_timings(speed)
        jams_on_route.append({
            "name":       loc["name"],
            "lat":        loc["lat"],
            "lon":        loc["lon"],
            "speed":      speed,
            "freeFlow":   freeflow,
            "status":     t["status"],
            "isHeavy":    speed < 15,
            "isModerate": 15 <= speed < 30,
        })

    heavy = [j for j in jams_on_route if j["isHeavy"]]
    has_heavy = len(heavy) > 0

    # Build a clear, actionable alternate route suggestion
    alternate_msg = ""
    alternate_tab = None  # which tab to suggest switching to
    if has_heavy:
        jam_names = " & ".join(j["name"] for j in heavy)
        if route_idx == 0:
            alternate_msg = (
                f"🔴 Heavy traffic detected at {jam_names} on the Fastest Route. "
                "Switch to the Alternate Route (Tab 2) — it bypasses this congestion via Rajpur Road "
                "and is likely faster right now."
            )
            alternate_tab = 1
        elif route_idx == 1:
            alternate_msg = (
                f"🔴 Heavy traffic at {jam_names} on the Alternate Route. "
                "Try the Shortest Route (Tab 3) via Ballupur Chowk / Chakrata Road instead."
            )
            alternate_tab = 2
        else:
            alternate_msg = (
                f"🔴 Heavy traffic at {jam_names}. "
                "All routes have some congestion — the Fastest Route (Tab 1) may still be quicker overall."
            )
            alternate_tab = 0

    return jsonify({
        "jamsOnRoute":  jams_on_route,
        "heavyCount":   len(heavy),
        "hasHeavy":     has_heavy,
        "alternateMsg": alternate_msg,
        "alternateTab": alternate_tab,
    })


# ── ROAD SEGMENTS API ─────────────────────────────────────────────────────────

@app.route("/road-segments")
def road_segments():
    """Return predefined road segment geometries for major Dehradun roads."""
    segments = [
        {
            "name": "Rajpur Road",
            "waypoints": [
                [30.3190, 78.0465], [30.3230, 78.0510], [30.3280, 78.0555],
                [30.3340, 78.0600], [30.3400, 78.0645], [30.3460, 78.0680],
                [30.3530, 78.0700], [30.3600, 78.0735]
            ]
        },
        {
            "name": "Haridwar Road",
            "waypoints": [
                [30.3180, 78.0410], [30.3100, 78.0350], [30.3030, 78.0280],
                [30.2960, 78.0200], [30.2887, 78.0110]
            ]
        },
        {
            "name": "Chakrata Road",
            "waypoints": [
                [30.3200, 78.0420], [30.3180, 78.0350], [30.3160, 78.0280],
                [30.3145, 78.0200], [30.3130, 78.0120], [30.3110, 78.0050]
            ]
        },
        {
            "name": "Sahastradhara Road",
            "waypoints": [
                [30.3400, 78.0645], [30.3420, 78.0730], [30.3440, 78.0810],
                [30.3460, 78.0880]
            ]
        },
        {
            "name": "GMS Road",
            "waypoints": [
                [30.3256, 78.0320], [30.3240, 78.0380], [30.3220, 78.0437],
                [30.3200, 78.0480]
            ]
        },
        {
            "name": "Rispana Bridge Road",
            "waypoints": [
                [30.3180, 78.0440], [30.3100, 78.0450], [30.3020, 78.0465],
                [30.2942, 78.0487]
            ]
        },
        {
            "name": "Ring Road",
            "waypoints": [
                [30.2887, 78.0110], [30.2860, 78.0230], [30.2870, 78.0350],
                [30.2900, 78.0440], [30.2942, 78.0487]
            ]
        },
        {
            "name": "Mussoorie Road",
            "waypoints": [
                [30.3600, 78.0735], [30.3680, 78.0760], [30.3770, 78.0780],
                [30.3860, 78.0790]
            ]
        },
    ]
    return jsonify(segments)


# ── GEOCODE API ───────────────────────────────────────────────────────────────

@app.route("/geocode")
def geocode():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"error": "q param required"}), 400

    try:
        url = (
            f"https://api.tomtom.com/search/2/search/{requests.utils.quote(query)}.json"
            f"?key={TOMTOM_KEY}&limit=1&countrySet=IN&lat=30.3165&lon=78.0322&radius=100000"
        )
        res = requests.get(url, timeout=4).json()
        results = res.get("results", [])
        if results:
            pos  = results[0]["position"]
            name = (results[0].get("poi", {}).get("name", "")
                    or results[0].get("address", {}).get("freeformAddress", query))
            return jsonify({"lat": pos["lat"], "lon": pos["lon"], "name": name})
    except Exception as e:
        print(f"[GEOCODE TomTom FAIL] {e}")

    try:
        res = requests.get(
            f"https://nominatim.openstreetmap.org/search"
            f"?q={requests.utils.quote(query)}&format=json&limit=1&countrycodes=in",
            timeout=4, headers={"User-Agent": "SmartTraffic-App/1.0"}
        ).json()
        if res:
            return jsonify({
                "lat": float(res[0]["lat"]),
                "lon": float(res[0]["lon"]),
                "name": res[0].get("display_name", query).split(",")[0]
            })
    except Exception as e:
        print(f"[GEOCODE Nominatim FAIL] {e}")

    return jsonify({"error": "Location not found"}), 404


# ── RUN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)