# Datos de ejemplo en memoria (sin base de datos)
pacientes = [
    {"id": 1, "nombre": "María López Hernández", "edad": 34, "sexo": "F", "telefono": "555-201-3344",
     "correo": "maria.lopez@correo.com", "sangre": "O+", "alergias": "Penicilina", "estado": "Activo"},
    {"id": 2, "nombre": "Carlos Ramírez Soto", "edad": 52, "sexo": "M", "telefono": "555-778-1020",
     "correo": "carlos.ramirez@correo.com", "sangre": "A+", "alergias": "Ninguna", "estado": "Activo"},
    {"id": 3, "nombre": "Ana Torres Gómez", "edad": 27, "sexo": "F", "telefono": "555-332-9011",
     "correo": "ana.torres@correo.com", "sangre": "B-", "alergias": "Ácaros", "estado": "En tratamiento"},
    {"id": 4, "nombre": "Jorge Méndez Ruiz", "edad": 61, "sexo": "M", "telefono": "555-901-4477",
     "correo": "jorge.mendez@correo.com", "sangre": "AB+", "alergias": "Sulfas", "estado": "Inactivo"},
]

medicos = [
    {"id": 1, "nombre": "Dra. Laura Castillo", "especialidad": "Medicina General", "consultorio": "101",
     "horario": "Lun–Vie 08:00–14:00", "disponible": True},
    {"id": 2, "nombre": "Dr. Roberto Vega", "especialidad": "Cardiología", "consultorio": "204",
     "horario": "Lun–Jue 10:00–18:00", "disponible": True},
    {"id": 3, "nombre": "Dra. Sofía Navarro", "especialidad": "Pediatría", "consultorio": "110",
     "horario": "Mar–Sáb 09:00–15:00", "disponible": False},
]

citas = [
    {"id": 1, "paciente": "María López Hernández", "medico": "Dra. Laura Castillo", "fecha": "2026-11-25",
     "hora": "09:00", "motivo": "Chequeo general", "estado": "Confirmada"},
    {"id": 2, "paciente": "Carlos Ramírez Soto", "medico": "Dr. Roberto Vega", "fecha": "2026-11-25",
     "hora": "11:30", "motivo": "Control de presión arterial", "estado": "Pendiente"},
    {"id": 3, "paciente": "Ana Torres Gómez", "medico": "Dra. Laura Castillo", "fecha": "2026-11-26",
     "hora": "10:00", "motivo": "Seguimiento de alergia", "estado": "Confirmada"},
    {"id": 4, "paciente": "Jorge Méndez Ruiz", "medico": "Dr. Roberto Vega", "fecha": "2026-11-20",
     "hora": "12:00", "motivo": "Electrocardiograma", "estado": "Cancelada"},
]

consultas = [
    {"id": 1, "paciente_id": 1, "fecha": "2026-10-12", "medico": "Dra. Laura Castillo",
     "diagnostico": "Faringitis aguda", "notas": "Reposo 3 días, hidratación."},
    {"id": 2, "paciente_id": 2, "fecha": "2026-11-02", "medico": "Dr. Roberto Vega",
     "diagnostico": "Hipertensión arterial controlada", "notas": "Continuar tratamiento."},
    {"id": 3, "paciente_id": 1, "fecha": "2026-08-30", "medico": "Dra. Laura Castillo",
     "diagnostico": "Revisión anual sin hallazgos", "notas": "Estudios de laboratorio normales."},
]

recetas = [
    {"id": 1, "paciente": "María López Hernández", "medico": "Dra. Laura Castillo", "fecha": "2026-10-12",
     "medicamentos": [{"nombre": "Ibuprofeno 400 mg", "dosis": "1 tableta cada 8 h por 3 días"},
                      {"nombre": "Paracetamol 500 mg", "dosis": "1 tableta cada 6 h si hay fiebre"}]},
    {"id": 2, "paciente": "Carlos Ramírez Soto", "medico": "Dr. Roberto Vega", "fecha": "2026-11-02",
     "medicamentos": [{"nombre": "Losartán 50 mg", "dosis": "1 tableta cada 24 h"}]},
]

facturas = [
    {"id": "F-1001", "paciente": "María López Hernández", "concepto": "Consulta general", "fecha": "2026-10-12",
     "monto": 450.00, "estado": "Pagada"},
    {"id": "F-1002", "paciente": "Carlos Ramírez Soto", "concepto": "Consulta cardiología", "fecha": "2026-11-02",
     "monto": 850.00, "estado": "Pagada"},
    {"id": "F-1003", "paciente": "Ana Torres Gómez", "concepto": "Pruebas de alergia", "fecha": "2026-11-18",
     "monto": 1200.00, "estado": "Pendiente"},
]
