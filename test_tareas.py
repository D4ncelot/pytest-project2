import pytest
from tareas import agregar_tarea, actualizar_tarea, marcar_completada, eliminar_tarea, listar_tareas, tareas

def setup_function():
    tareas.clear()

def test_agregar():
    agregar_tarea(1, "Comprar Mercaderia", "Ir a la tienda y comprar cosas", "Alta")
    assert actualizar_tarea(1, "Lavar Ropa", "Lavar y secar la ropa", "Media")
    with pytest.raises(ValueError):
        assert agregar_tarea(1, "Comprar Comida", "Ir a la tienda y comprar cosas", "Alta") # Ya existe

def test_actualizar():
    agregar_tarea(2, "Comprar Mercaderia", "Ir a la tienda y comprar cosas", "Alta")
    assert actualizar_tarea(2, "Pasear al Perro", "Salir a pasear", "Muy Alta")
    with pytest.raises(KeyError):
        assert actualizar_tarea(45, "Pasear al Perro", "Salir a pasear", "Muy Alta") # El index no existe

def test_marcar():
    agregar_tarea(1, "Comprar Mercaderia", "Ir a la tienda y comprar cosas", "Alta")
    assert marcar_completada(1)
    with pytest.raises(KeyError):
        assert marcar_completada(12) # No existe

def test_eliminar():
    agregar_tarea(1, "Comprar Mercaderia", "Ir a la tienda y comprar cosas", "Alta")
    assert eliminar_tarea(1)
    with pytest.raises(KeyError):
        assert eliminar_tarea(44) # No existe

def test_listar():
    agregar_tarea(1, "Comprar Mercaderia", "Ir a la tienda y comprar cosas", "Alta")
    agregar_tarea(2, "Pasear al Perro", "Salir a pasear", "Muy Alta")
    assert listar_tareas(False)