from datetime import date

from flask import Flask, abort, redirect, render_template, url_for

import datos

app = Flask(__name__, static_folder="estaticos")
app.secret_key = "clave-secreta-de-desarrollo"


def buscar(lista, id_):
    for elemento in lista:
        if elemento["id"] == id_:
            return elemento
    abort(404)


@app.context_processor
def variables_globales():
    return {"usuario": None, "hoy": date.today().isoformat()}


# ---------- Acceso ----------
@app.route("/")
def inicio():
    return redirect(url_for("iniciar_sesion"))


@app.route("/iniciar-sesion", methods=["GET", "POST"])
def iniciar_sesion():
    return render_template("login.html")


@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render_template("registro.html")


@app.route("/recuperar-contrasena", methods=["GET", "POST"])
def recuperar_contrasena():
    return render_template("recuperar_contrasena.html")


@app.route("/cerrar-sesion")
def cerrar_sesion():
    return redirect(url_for("iniciar_sesion"))


# ---------- Panel ----------
@app.route("/panel")
def panel():
    resumen = {
        "pacientes": len(datos.pacientes),
        "citas": len(datos.citas),
        "medicos": len(datos.medicos),
        "pendiente": sum(f["monto"] for f in datos.facturas if f["estado"] == "Pendiente"),
    }
    return render_template("index.html", resumen=resumen, citas=datos.citas[:5])


# ---------- Pacientes ----------
@app.route("/pacientes")
def pacientes():
    return render_template("lista_pacientes.html", pacientes=datos.pacientes, q="")


@app.route("/pacientes/nuevo", methods=["GET", "POST"])
def nuevo_paciente():
    return render_template("nuevo_paciente.html")


@app.route("/pacientes/<int:id>")
def expediente_paciente(id):
    paciente = buscar(datos.pacientes, id)
    historial = [c for c in datos.consultas if c["paciente_id"] == id]
    citas = [c for c in datos.citas if c["paciente"] == paciente["nombre"]]
    return render_template("expediente_paciente.html", paciente=paciente,
                           historial=historial, citas=citas)


# ---------- Citas ----------
@app.route("/citas")
def citas():
    return render_template("agenda_citas.html", citas=datos.citas, estado="")


@app.route("/citas/nueva", methods=["GET", "POST"])
def nueva_cita():
    return render_template("nueva_cita.html", pacientes=datos.pacientes, medicos=datos.medicos)


@app.route("/citas/<int:id>/cancelar", methods=["POST"])
def cancelar_cita(id):
    return redirect(url_for("citas"))


# ---------- Médicos ----------
@app.route("/medicos")
def medicos():
    return render_template("lista_medicos.html", medicos=datos.medicos)


# ---------- Consultas ----------
@app.route("/consultas/nueva", methods=["GET", "POST"])
def nueva_consulta():
    return render_template("nueva_consulta.html", pacientes=datos.pacientes,
                           medicos=datos.medicos, seleccionado=None)


# ---------- Recetas ----------
@app.route("/recetas")
def recetas():
    return render_template("lista_recetas.html", recetas=datos.recetas)


@app.route("/recetas/<int:id>")
def ver_receta(id):
    return render_template("ver_receta.html", receta=buscar(datos.recetas, id))


# ---------- Facturación ----------
@app.route("/facturacion")
def facturacion():
    total = sum(f["monto"] for f in datos.facturas)
    pagado = sum(f["monto"] for f in datos.facturas if f["estado"] == "Pagada")
    return render_template("lista_facturas.html", facturas=datos.facturas,
                           total=total, pagado=pagado)


# ---------- Cuenta ----------
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route("/configuracion", methods=["GET", "POST"])
def configuracion():
    return render_template("configuracion.html")


@app.errorhandler(404)
def no_encontrado(_):
    return render_template("error_404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
