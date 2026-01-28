import os

# Definimos la ruta base como 'frontend' para respetar tu estructura
base_dir = "frontend"

# Mapa de archivos adaptado a tu estructura de VS Code (screens, components/layout)
project_structure = {
    # Archivos de configuración en la raíz de 'frontend'
    f"{base_dir}/package.json": """{
  "name": "central-esterilizacion-front",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.0",
    "lucide-react": "^0.344.0",
    "recharts": "^2.12.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.1"
  },
  "devDependencies": {
    "@types/react": "^18.2.64",
    "@types/react-dom": "^18.2.21",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.18",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "vite": "^5.1.4"
  }
}""",
    f"{base_dir}/vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})""",
    f"{base_dir}/tailwind.config.js": """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#0ea5e9',
          dark: '#0284c7',
        },
        secondary: '#64748b',
        success: '#10b981',
        danger: '#ef4444',
      }
    },
  },
  plugins: [],
}""",
    f"{base_dir}/postcss.config.js": """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}""",
    f"{base_dir}/index.html": """<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Central de Esterilización</title>
  </head>
  <body class="bg-slate-50 text-slate-900 antialiased">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>""",

    # Estilos Globales
    f"{base_dir}/src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply font-sans;
  }
}""",

    # Punto de entrada React
    f"{base_dir}/src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",

    # App.jsx (Ruteo) - Adaptado para importar desde 'screens' y 'components/layout'
    f"{base_dir}/src/App.jsx": """import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import MainLayout from './components/layout/MainLayout';
import DashboardScreen from './screens/DashboardScreen';
import SterilizationCycleScreen from './screens/SterilizationCycleScreen';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard" element={<DashboardScreen />} />
          <Route path="ciclo" element={<SterilizationCycleScreen />} />
          
          <Route path="hojas-vida" element={<div className="p-8">Hojas de vida - En construcción</div>} />
          <Route path="reporte" element={<div className="p-8">Reporte - En construcción</div>} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;""",

    # Layout Principal (Navbar) - Va en tu carpeta src/components/layout
    f"{base_dir}/src/components/layout/MainLayout.jsx": """import React, { useState } from 'react';
import { Outlet, useLocation, Link } from 'react-router-dom';
import { LayoutDashboard, RefreshCw, FileText, ClipboardList, Settings, Bell, ChevronDown, ChevronUp } from 'lucide-react';

const MainLayout = () => {
  const location = useLocation();
  const [openDropdown, setOpenDropdown] = useState(null);

  const toggleDropdown = (name) => {
    setOpenDropdown(openDropdown === name ? null : name);
  };

  const NavItem = ({ to, icon: Icon, label, dropdownItems, name }) => {
    const isActive = location.pathname.includes(to) && !dropdownItems;
    const isDropdownOpen = openDropdown === name;

    if (dropdownItems) {
      return (
        <div className="relative group">
          <button 
            onClick={() => toggleDropdown(name)}
            className={`flex items-center gap-2 px-3 py-2 rounded-md text-white/90 hover:text-white hover:bg-white/10 transition-colors ${isDropdownOpen ? 'bg-white/10 font-medium' : ''}`}
          >
            {Icon && <Icon size={18} />}
            <span>{label}</span>
            {isDropdownOpen ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
          </button>
          
          {isDropdownOpen && (
            <div className="absolute top-full left-0 mt-1 w-56 bg-white rounded-lg shadow-xl border border-slate-100 py-2 z-50 text-slate-700">
              {dropdownItems.map((item, idx) => (
                <Link 
                  key={idx} 
                  to={item.to || '#'} 
                  className="block px-4 py-2 hover:bg-slate-50 hover:text-primary text-sm transition-colors"
                  onClick={() => setOpenDropdown(null)}
                >
                  {item.label}
                </Link>
              ))}
            </div>
          )}
        </div>
      );
    }

    return (
      <Link 
        to={to} 
        className={`flex items-center gap-2 px-3 py-2 rounded-md transition-colors ${isActive ? 'text-white font-bold bg-white/20' : 'text-white/80 hover:text-white hover:bg-white/10'}`}
      >
        {Icon && <Icon size={18} />}
        <span>{label}</span>
      </Link>
    );
  };

  return (
    <div className="min-h-screen bg-slate-100 flex flex-col">
      <header className="bg-gradient-to-r from-blue-500 to-cyan-400 text-white shadow-md">
        <div className="px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-8">
            <div className="font-bold text-lg tracking-wider">CENTRAL DE ESTERILIZACIÓN</div>
            <nav className="hidden md:flex items-center gap-1">
              <NavItem to="/dashboard" icon={LayoutDashboard} label="Dashboard" />
              <NavItem 
                name="ciclo"
                label="Ciclo Esterilización" 
                icon={RefreshCw}
                dropdownItems={[
                  { label: 'Trazabilidad Qx', to: '/ciclo' },
                  { label: 'Instrumentos Qx', to: '/ciclo' },
                  { label: 'Insumos Qx', to: '/ciclo' },
                  { label: 'Histórico de ciclo', to: '/ciclo' }
                ]}
              />
              <NavItem to="/hojas-vida" icon={FileText} label="Hojas de vida" />
              <NavItem to="/reporte" icon={ClipboardList} label="Reporte" />
              <NavItem 
                name="config"
                label="Configuración" 
                icon={Settings}
                dropdownItems={[
                  { label: 'Insumos Quirúrgicos' }, { label: 'Proveedores' }, { label: 'Especialidad' }, { label: 'Sedes' }, { label: 'Usuarios' }
                ]}
              />
            </nav>
          </div>
          <div className="flex items-center gap-4">
            <button className="p-2 hover:bg-white/20 rounded-full relative">
              <Bell size={20} />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-red-400 rounded-full border border-blue-500"></span>
            </button>
            <div className="flex items-center gap-3 pl-4 border-l border-white/20">
              <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Juan" alt="Avatar" className="w-9 h-9 rounded-full bg-white/20 p-0.5"/>
              <span className="font-medium text-sm hidden lg:block">Juan Pablo C.</span>
              <ChevronDown size={16} className="opacity-70" />
            </div>
          </div>
        </div>
      </header>
      <main className="flex-1 p-6 overflow-y-auto">
        <Outlet />
      </main>
    </div>
  );
};

export default MainLayout;""",

    # Screen 1: Dashboard - Va en tu carpeta src/screens
    f"{base_dir}/src/screens/DashboardScreen.jsx": """import React from 'react';

const DashboardScreen = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-slate-800">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h3 className="text-slate-500 text-sm font-medium mb-2">Efectividad Global</h3>
          <div className="flex items-end gap-2">
            <span className="text-4xl font-bold text-slate-800">90%</span>
            <span className="text-emerald-500 text-sm font-medium mb-1">↑ 2.5%</span>
          </div>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h3 className="text-slate-500 text-sm font-medium mb-2">Mantenimientos</h3>
          <div className="text-4xl font-bold text-blue-500">4,509</div>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h3 className="text-slate-500 text-sm font-medium mb-2">Reportes Totales</h3>
          <div className="text-4xl font-bold text-slate-800">3,712</div>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
          <h3 className="text-slate-500 text-sm font-medium mb-2">Total Instrumentos</h3>
          <div className="text-4xl font-bold text-cyan-500">15,700</div>
        </div>
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
         {/* Placeholder de Gráficos */}
         <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100 h-80 flex flex-col justify-center items-center text-slate-400">
            <p>Gráfico de Tiempos (Box Plot)</p>
         </div>
         <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-100 h-80 flex flex-col justify-center items-center text-slate-400">
            <p>Gráfico de Repeticiones (Barras)</p>
         </div>
      </div>
    </div>
  );
};

export default DashboardScreen;""",

    # Screen 2: Ciclo de Esterilización (Scanner) - Va en src/screens
    f"{base_dir}/src/screens/SterilizationCycleScreen.jsx": """import React, { useState } from 'react';
import { Search, CheckCircle2, AlertCircle, Camera } from 'lucide-react';

const SterilizationCycleScreen = () => {
  const [activeStep, setActiveStep] = useState(0);
  
  const steps = [
    { id: 'recepcion', label: 'Recepción' },
    { id: 'lavado', label: 'Lavado' },
    { id: 'secado', label: 'Secado' },
    { id: 'sellado', label: 'Sellado' },
    { id: 'rotulado', label: 'Rotulado' },
    { id: 'esterilizado', label: 'Esterilizado' },
  ];

  const goodItems = [
    { name: 'Bisturí de córnea', qty: 1 },
    { name: 'Blefaróstato de Barraquer', qty: 1 },
    { name: 'Pinzas de iris', qty: 1 },
    { name: 'Portaagujas de Barraquer', qty: 1 },
  ];

  const badItems = [
    { name: 'Espátula de iris', qty: 2 },
    { name: 'Ganchos de iris', qty: 2 },
  ];

  return (
    <div className="flex h-[calc(100vh-8rem)] gap-6">
      <div className="w-16 lg:w-64 bg-white rounded-xl shadow-sm border border-slate-100 hidden md:block overflow-hidden">
        <div className="p-4 border-b border-slate-100">
            <div className="relative">
                <Search className="absolute left-3 top-2.5 text-slate-400" size={18} />
                <input type="text" placeholder="Buscar..." className="w-full bg-slate-50 pl-10 pr-4 py-2 rounded-lg text-sm outline-none focus:ring-2 focus:ring-blue-100"/>
            </div>
        </div>
        <div className="py-2">
            {steps.map((step, idx) => (
                <button 
                    key={step.id}
                    onClick={() => setActiveStep(idx)}
                    className={`w-full text-left px-6 py-4 flex items-center gap-3 ${idx === activeStep ? 'text-blue-600 bg-blue-50 border-r-4 border-blue-500' : 'text-slate-500 hover:bg-slate-50'}`}
                >
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center ${idx === activeStep ? 'bg-blue-100' : 'bg-slate-100'}`}>
                        <span className="text-xs font-bold">{idx + 1}</span>
                    </div>
                    <span className="font-medium">{step.label}</span>
                </button>
            ))}
        </div>
      </div>
      <div className="flex-1 flex flex-col gap-6 overflow-hidden">
        <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-100 flex flex-wrap gap-4 text-sm text-slate-600 justify-between items-center">
            <div className="flex gap-6">
                <div>
                    <span className="block text-xs text-slate-400">Quirófano</span>
                    <span className="font-semibold text-slate-800">Quirófano 8</span>
                </div>
                <div className="w-px bg-slate-200 h-8"></div>
                <div>
                    <span className="block text-xs text-slate-400">Especialidad</span>
                    <span className="font-semibold text-slate-800">Oftalmología</span>
                </div>
                <div className="w-px bg-slate-200 h-8"></div>
                <div>
                    <span className="block text-xs text-slate-400">Kit</span>
                    <span className="font-semibold text-slate-800 text-blue-600">KIT 01</span>
                </div>
            </div>
            <div>
                 <span className="text-xs bg-slate-100 px-2 py-1 rounded text-slate-500">ID: 02/12/2025-Q1</span>
            </div>
        </div>
        <div className="flex-1 flex gap-6 min-h-0">
            <div className="flex-1 bg-white rounded-xl shadow-sm border border-slate-100 p-4 flex flex-col relative">
                <div className="bg-red-50 border border-red-100 text-red-600 px-4 py-3 rounded-lg flex justify-between items-start mb-4">
                    <div className="flex gap-3">
                        <AlertCircle className="shrink-0 mt-0.5" size={18} />
                        <div className="text-sm">
                            <span className="font-bold block">Alerta: Faltan instrumentos</span>
                            <span className="opacity-80">Por favor, escanea o reporta los elementos pendientes.</span>
                        </div>
                    </div>
                </div>
                <div className="flex-1 bg-slate-50 rounded-lg border-2 border-dashed border-slate-200 flex flex-col items-center justify-center relative overflow-hidden group">
                    <div className="absolute inset-0 bg-emerald-900/5 flex items-center justify-center">
                        <p className="text-slate-400 font-medium">Vista de Cámara / Detección IA</p>
                    </div>
                    <div className="absolute top-1/4 left-1/4 w-32 h-64 border-2 border-emerald-400 bg-emerald-400/10 rounded"></div>
                    <div className="absolute top-1/3 right-1/3 w-24 h-48 border-2 border-red-400 bg-red-400/10 rounded"></div>
                    <button className="absolute bottom-6 bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-full shadow-lg flex items-center gap-2 transition-transform active:scale-95">
                        <Camera size={18} />
                        Escanear
                    </button>
                </div>
            </div>
            <div className="w-80 flex flex-col gap-4 overflow-y-auto">
                <div className="bg-white rounded-xl shadow-sm border border-slate-100 p-4">
                    <h3 className="text-emerald-600 font-bold mb-3 flex items-center gap-2">
                        <CheckCircle2 size={18} /> Buen estado
                    </h3>
                    <div className="space-y-0">
                        {goodItems.map((item, i) => (
                            <div key={i} className="flex justify-between items-center py-3 border-b border-slate-50 last:border-0 text-sm">
                                <span className="text-slate-600 flex items-center gap-2">
                                    <span className="w-1.5 h-1.5 rounded-full bg-slate-300"></span>
                                    {item.name}
                                </span>
                                <span className="bg-slate-100 px-2 py-0.5 rounded text-xs text-slate-500">{item.qty}</span>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="bg-white rounded-xl shadow-sm border border-slate-100 p-4 border-l-4 border-l-red-400">
                    <h3 className="text-red-500 font-bold mb-3 flex items-center gap-2">
                        <AlertCircle size={18} /> Mal estado
                    </h3>
                    <div className="space-y-0">
                        {badItems.map((item, i) => (
                            <div key={i} className="flex justify-between items-center py-3 border-b border-slate-50 last:border-0 text-sm">
                                <span className="text-slate-600 flex items-center gap-2">
                                    <span className="w-1.5 h-1.5 rounded-full bg-red-200"></span>
                                    {item.name}
                                </span>
                                <span className="bg-red-50 text-red-600 px-2 py-0.5 rounded text-xs border border-red-100">{item.qty}</span>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="mt-auto flex gap-2 pt-2">
                    <button className="flex-1 px-4 py-2 rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-50 text-sm font-medium">Atrás</button>
                    <button className="flex-1 px-4 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-white shadow-sm shadow-emerald-200 text-sm font-medium">Guardar</button>
                </div>
            </div>
        </div>
      </div>
    </div>
  );
};

export default SterilizationCycleScreen;"""
}

def fill_frontend():
    print(f"🚀 Iniciando configuración en la carpeta '{base_dir}'...")
    
    if not os.path.exists(base_dir):
        print(f"⚠️ La carpeta '{base_dir}' no existe. Creándola...")
        os.makedirs(base_dir)

    for file_path, content in project_structure.items():
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Archivo creado/actualizado: {file_path}")

    print("\\n✨ ¡Estructura Frontend completada!")
    print("------------------------------------------------")
    print("IMPORTANTE - Siguientes pasos:")
    print(f"1. Abre la terminal en VS Code.")
    print(f"2. Entra a la carpeta frontend: cd {base_dir}")
    print("3. Instala dependencias: npm install")
    print("4. Ejecuta el proyecto: npm run dev")
    print("------------------------------------------------")

if __name__ == "__main__":
    fill_frontend()