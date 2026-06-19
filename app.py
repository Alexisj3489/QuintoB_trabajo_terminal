from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reloj Digital</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            overflow:hidden;
            /* Nuevo fondo: Gradiente de atardecer neón */
            background:linear-gradient(-45deg, #0b0914, #2b1055, #75205d, #b93c52);
            background-size:400% 400%;
            animation:gradient 12s ease infinite;
        }

        @keyframes gradient{
            0%{background-position:0% 50%;}
            50%{background-position:100% 50%;}
            100%{background-position:0% 50%;}
        }

        .card{
            /* Tarjeta de cristal más oscura con bordes rosados */
            background:rgba(0, 0, 0, 0.4);
            backdrop-filter:blur(20px);
            -webkit-backdrop-filter:blur(20px);
            border:1px solid rgba(255, 107, 152, 0.3);
            border-radius:30px;
            padding:50px;
            text-align:center;
            box-shadow:0 15px 35px rgba(0,0,0,0.5), 0 0 20px rgba(255, 107, 152, 0.1);
            width:90%;
            max-width:700px;
            z-index: 10;
        }

        h1{
            color:#f8f8f8;
            font-size:2.2rem;
            margin-bottom:20px;
            letter-spacing:4px;
            text-transform: uppercase;
        }

        .clock{
            /* Efecto Neón naranja/rosado para los números */
            color:#ff9a9e;
            font-size:5.5rem;
            font-weight:900;
            text-shadow: 0 0 10px rgba(255, 154, 158, 0.8), 0 0 30px rgba(233, 64, 87, 0.6);
            margin:20px 0;
            letter-spacing: 2px;
        }

        .date{
            color:#fca5a5;
            font-size:1.5rem;
            margin-top:10px;
            font-weight: 300;
            letter-spacing: 1px;
        }

        .subtitle{
            color:#cbd5e1;
            margin-top:30px;
            font-size:1rem;
            opacity: 0.7;
        }

        /* Cambiamos los círculos por formas flotantes con brillo */
        .circle{
            position:absolute;
            background:linear-gradient(135deg, rgba(255,107,152,0.15), rgba(255,160,122,0.05));
            border: 1px solid rgba(255, 107, 152, 0.2);
            animation:float 12s infinite ease-in-out;
            border-radius: 15px; /* Bordes redondeados pero no círculos perfectos */
            transform: rotate(45deg);
        }

        .circle:nth-child(1){
            width:250px;
            height:250px;
            top:5%;
            left:5%;
        }

        .circle:nth-child(2){
            width:180px;
            height:180px;
            bottom:10%;
            right:10%;
            animation-duration:16s;
            animation-delay: -2s;
            border-radius: 50%; /* Este se queda como círculo para contrastar */
        }

        .circle:nth-child(3){
            width:120px;
            height:120px;
            top:60%;
            left:15%;
            animation-duration:14s;
            animation-delay: -5s;
        }

        @keyframes float{
            0%,100%{
                transform:translateY(0px) rotate(45deg);
            }
            50%{
                transform:translateY(-40px) rotate(60deg);
            }
        }

        @media(max-width:768px){
            .clock{
                font-size:3.5rem;
            }

            .date{
                font-size:1.1rem;
            }

            h1{
                font-size:1.8rem;
            }
        }
    </style>
</head>
<body>

<div class="circle"></div>
<div class="circle"></div>
<div class="circle"></div>

<div class="card">
    <h1>🕒 RELOJ DIGITAL</h1>

    <div id="clock" class="clock">00:00:00</div>

    <div id="date" class="date"></div>

    <div class="subtitle">
        Landing Page desarrollada con Flask
    </div>
</div>

<script>

function actualizarReloj(){

    const ahora = new Date();

    const hora = String(ahora.getHours()).padStart(2,'0');
    const minuto = String(ahora.getMinutes()).padStart(2,'0');
    const segundo = String(ahora.getSeconds()).padStart(2,'0');

    document.getElementById("clock").innerHTML =
        `${hora}:${minuto}:${segundo}`;

    const opciones = {
        weekday:'long',
        year:'numeric',
        month:'long',
        day:'numeric'
    };

    document.getElementById("date").innerHTML =
        ahora.toLocaleDateString('es-ES', opciones);
}

actualizarReloj();
setInterval(actualizarReloj,1000);

</script>

</body>
</html>
"""

#Ruta principal
@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)