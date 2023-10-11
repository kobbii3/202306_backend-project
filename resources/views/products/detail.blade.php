@extends('layout.main')

@section('content')
    <h1 class="text-center">Detalle del Producto</h1>

    <div class="container">
        <div class="row">
            <div class="col-md-8">
                <img src="img/producto1.png"  class="img-fluid">
            </div>
            <div class="col-md-4">
                <h1>nombre del producto</h1>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Porro sint expedita officiis sit doloremque maiores adipisci culpa qui impedit ea officia harum quos, sapiente nulla. Nobis odio eius sed dolore!</p>
                <h3>$1.250.000</h3>
                <button type="button" class="btn my-background">Añadir al carrito</button>
            </div>
        </div>
    </div>
@endsection