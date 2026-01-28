import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Hammer } from 'lucide-react'; 

// --- NUEVO IMPORT: LOGIN ---
import LoginScreen from './screens/LoginScreen';

// Layout y Pantallas Principales
import MainLayout from './components/layout/MainLayout';
import DashboardScreen from './screens/DashboardScreen';
import SterilizationCycleScreen from './screens/SterilizationCycleScreen';
import InformesScreen from './screens/InformesScreen'; 
import ReportesScreen from './screens/ReportesScreen'; 

// --- IMPORT: HOJAS DE VIDA ---
import HojasDeVidaScreen from './screens/HojasDeVidaScreen';

// Configuración
import InsumosScreen from './screens/config/InsumosScreen';
import ProveedoresScreen from './screens/config/ProveedoresScreen';
import EspecialidadScreen from './screens/config/EspecialidadScreen';
import SubespecialidadScreen from './screens/config/SubespecialidadScreen';
import TipoSubespecialidadScreen from './screens/config/TipoSubespecialidadScreen';
// --- IMPORT: KIT ---
import KitScreen from './screens/config/KitScreen';

import SedesScreen from './screens/config/SedesScreen';
import QuirofanoScreen from './screens/config/QuirofanoScreen';
import UsuariosScreen from './screens/config/UsuariosScreen';

// Informes
import IngresoInstrumentosScreen from './screens/informes/IngresoInstrumentosScreen';
import DevolucionInstrumentosScreen from './screens/informes/DevolucionInstrumentosScreen';
import IndicadorBiologicoScreen from './screens/informes/IndicadorBiologicoScreen';
import IndicadorGasScreen from './screens/informes/IndicadorGasScreen';
import IndicadorPaquetesScreen from './screens/informes/IndicadorPaquetesScreen';
import HistorialTrasladosScreen from './screens/informes/HistorialTrasladosScreen';
import IndicadorPrimeraCargaScreen from './screens/informes/IndicadorPrimeraCargaScreen';
import RegistroEsterilizacionScreen from './screens/informes/RegistroEsterilizacionScreen';

// Ciclo
import TrazabilidadScreen from './screens/ciclo/TrazabilidadScreen';
import HistoricoCicloScreen from './screens/ciclo/HistoricoCicloScreen';
// --- IMPORT: ALMACENAMIENTO ---
import AlmacenamientoScreen from './screens/ciclo/AlmacenamientoScreen';

const PlaceholderPage = ({ title }) => (
  <div className="flex flex-col items-center justify-center h-[60vh] text-slate-400 space-y-4">
    <div className="p-6 bg-slate-100 rounded-full"><Hammer size={48} className="text-slate-300" /></div>
    <h2 className="text-2xl font-bold text-slate-600">{title}</h2>
  </div>
);

function App() {
  return (
    <Router>
      <Routes>
        
        {/* 1. RUTA PÚBLICA: LOGIN (Sin Layout) */}
        <Route path="/login" element={<LoginScreen />} />

        {/* 2. REDIRECCIÓN INICIAL: Raíz -> Login */}
        <Route path="/" element={<Navigate to="/login" replace />} />

        {/* 3. RUTAS PROTEGIDAS (Dentro de MainLayout) */}
        <Route element={<MainLayout />}>
          
          {/* Dashboard y Pantallas Principales */}
          <Route path="/dashboard" element={<DashboardScreen />} />
          <Route path="/informes" element={<InformesScreen />} />
          <Route path="/reporte" element={<ReportesScreen />} />
          
          {/* Hojas de Vida */}
          <Route path="/hojas-vida" element={<HojasDeVidaScreen />} />

          {/* Rutas de Informes */}
          <Route path="/informes/ingreso-instrumentos" element={<IngresoInstrumentosScreen />} />
          <Route path="/informes/devolucion-instrumentos" element={<DevolucionInstrumentosScreen />} />
          <Route path="/informes/indicador-biologico" element={<IndicadorBiologicoScreen />} />
          <Route path="/informes/indicador-gas" element={<IndicadorGasScreen />} />
          <Route path="/informes/indicador-paquetes" element={<IndicadorPaquetesScreen />} />
          <Route path="/informes/historial-traslados" element={<HistorialTrasladosScreen />} />
          <Route path="/informes/indicador-primera-carga" element={<IndicadorPrimeraCargaScreen />} />
          <Route path="/informes/registro-esterilizacion" element={<RegistroEsterilizacionScreen />} />

          {/* Rutas de Ciclo */}
          <Route path="/ciclo/trazabilidad" element={<TrazabilidadScreen />} />
          <Route path="/ciclo/instrumentos" element={<SterilizationCycleScreen />} />
          <Route path="/ciclo/insumos" element={<PlaceholderPage title="Insumos Qx" />} />
          <Route path="/ciclo/historico" element={<HistoricoCicloScreen />} />
          <Route path="/ciclo/tablero" element={<PlaceholderPage title="Tablero de ciclos" />} />
          
          {/* Ruta: Almacenamiento */}
          <Route path="/ciclo/almacenamiento" element={<AlmacenamientoScreen />} />

          {/* Rutas de Configuración */}
          <Route path="/config/insumos" element={<InsumosScreen />} />
          <Route path="/config/proveedores" element={<ProveedoresScreen />} />
          <Route path="/config/especialidad" element={<EspecialidadScreen />} />
          <Route path="/config/subespecialidad" element={<SubespecialidadScreen />} />
          <Route path="/config/tipo-subespecialidad" element={<TipoSubespecialidadScreen />} />
          
          {/* Config: Kit */}
          <Route path="/config/kit" element={<KitScreen />} />
          
          <Route path="/config/sedes" element={<SedesScreen />} />
          <Route path="/config/quirofano" element={<QuirofanoScreen />} />
          <Route path="/config/usuarios" element={<UsuariosScreen />} />

        </Route>
      </Routes>
    </Router>
  );
}

export default App;