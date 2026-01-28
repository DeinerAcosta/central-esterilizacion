import React from 'react';
import { Link } from 'react-router-dom';
// Importamos los nuevos íconos Microwave y WashingMachine
import {
  Download,
  Upload,
  Microwave,   // Nuevo ícono para "statim"
  WashingMachine, // Nuevo ícono visualmente similar al de "gas"
  Scissors,
  History,
  BarChart3,
  ClipboardList
} from 'lucide-react';

const InformesScreen = () => {
  const reportOptions = [
    {
      title: 'Ingreso de instrumentos de 3ros',
      icon: Download, // Este ya coincidía bien con la imagen
      to: '/informes/ingreso-instrumentos'
    },
    {
      title: 'Salida de instrumentos de 3ros',
      icon: Upload, // Este ya coincidía bien con la imagen
      to: '/informes/devolucion-instrumentos'
    },
    {
      title: 'Indicador biológico statim a gas',
      icon: Microwave, // Cambiado: se parece más al hornito de la imagen
      to: '/informes/indicador-biologico'
    },
    {
      title: 'Indicador a gas',
      icon: WashingMachine, // Cambiado: es el más parecido visualmente a la máquina de la foto
      to: '/informes/indicador-gas'
    },
    {
      title: 'Indicadores de paquetes e instrumentales',
      icon: Scissors, // Se mantiene: la imagen muestra tijeras y bisturí, este es el mejor aproximado único de la librería.
      to: '/informes/indicador-paquetes'
    },
    {
      title: 'Historial de traslados',
      icon: History, // Este ya coincidía perfecto
      to: '/informes/historial-traslados'
    },
    {
      title: 'Indicador de primera carga',
      icon: BarChart3, // Se mantiene: es una buena representación gráfica del concepto.
      to: '/informes/indicador-primera-carga'
    },
    {
      title: 'Registro de esterilización',
      icon: ClipboardList, // Este ya coincidía muy bien
      to: '/informes/registro-esterilizacion'
    },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-blue-500">Informes</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {reportOptions.map((item, index) => (
          <Link
            key={index}
            to={item.to}
            className="bg-white p-8 rounded-[2.5rem] shadow-sm hover:shadow-md transition-all duration-300 border border-slate-50 group flex flex-col items-center justify-center text-center h-64 gap-6 cursor-pointer"
          >
            {/* Se mantiene el strokeWidth en 1.5 para el estilo delgado de la foto */}
            <div className="text-slate-400 group-hover:text-blue-500 transition-colors transform group-hover:scale-110 duration-300">
              <item.icon strokeWidth={1.5} size={64} />
            </div>
            <div className="space-y-1">
              <h3 className="font-bold text-slate-400 text-lg leading-tight group-hover:text-slate-600 transition-colors">
                {item.title}
              </h3>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default InformesScreen;