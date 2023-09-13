<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('producto', function () {
    return "TOCHADA";
});

Route::get('producto/create', function () {
    return "AQUI VA A ESTAR EL FORMULARIO DE LA CREACION DE PRODUCTOS";
});

Route::get('producto/{id}/{categoria}', function ($id, $categoria) {
    return "el nombre del producto es $id con la categoria $categoria";
});
