import React, { useState } from 'react';
import { Mail, Lock, Eye, EyeOff, ArrowRight, Activity } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';

const LoginScreen = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // Aquí iría la lógica de autenticación real
    console.log("Iniciando sesión con:", email, password);
    navigate('/dashboard'); // Redirigir al dashboard
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-slate-50 font-sans p-4">
      
      {/* Tarjeta Principal */}
      <div className="bg-white w-full max-w-5xl h-[650px] rounded-[30px] shadow-2xl overflow-hidden flex flex-col md:flex-row animate-in fade-in zoom-in-95 duration-300">
        
        {/* SECCIÓN IZQUIERDA: IMAGEN Y BRANDING */}
        <div className="hidden md:flex w-1/2 relative flex-col justify-end p-12 text-white">
          {/* Imagen de fondo */}
          <div className="absolute inset-0 z-0">
             <img 
               src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=2053&auto=format&fit=crop" 
               alt="Hospital Sterilization" 
               className="w-full h-full object-cover"
             />
             {/* Overlay Gradiente Azul/Verde (Identidad de marca) */}
             <div className="absolute inset-0 bg-gradient-to-t from-blue-900/90 via-blue-800/60 to-transparent mix-blend-multiply"></div>
          </div>

          {/* Contenido sobre la imagen */}
          <div className="relative z-10 space-y-4">
            <div className="w-16 h-16 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center border border-white/30 mb-2">
                <Activity size={32} className="text-white" />
            </div>
            <h2 className="text-4xl font-bold leading-tight">Gestión Integral de <br/>Esterilización</h2>
            <p className="text-blue-100 text-sm font-medium opacity-90 max-w-sm">
              Control eficiente de ciclos, trazabilidad de instrumental e insumos quirúrgicos.
            </p>
          </div>
        </div>

        {/* SECCIÓN DERECHA: FORMULARIO */}
        <div className="w-full md:w-1/2 flex flex-col justify-center px-8 md:px-16 py-12 relative">
          
          {/* Logo móvil (Solo visible en pantallas pequeñas) */}
          <div className="md:hidden flex justify-center mb-8">
             <div className="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center text-white">
                <Activity size={24} />
             </div>
          </div>

          <div className="mb-10 text-center md:text-left">
            <h3 className="text-3xl font-extrabold text-slate-800 mb-2">Bienvenido</h3>
            <p className="text-slate-400 text-sm">Por favor, ingrese sus credenciales para continuar.</p>
          </div>

          <form onSubmit={handleLogin} className="space-y-6">
            
            {/* Input Usuario */}
            <div className="space-y-2">
              <label className="text-sm font-bold text-slate-700 ml-2">Correo electrónico</label>
              <div className="relative group">
                <div className="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
                  <Mail size={18} className="text-slate-400 group-focus-within:text-blue-500 transition-colors" />
                </div>
                <input 
                  type="email" 
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full h-14 bg-slate-50 border border-slate-200 text-slate-600 text-sm rounded-full pl-12 pr-6 outline-none focus:border-blue-400 focus:bg-white focus:ring-4 focus:ring-blue-50 transition-all placeholder:text-slate-300"
                  placeholder="ejemplo@correo.com"
                  required
                />
              </div>
            </div>

            {/* Input Contraseña */}
            <div className="space-y-2">
               <div className="flex justify-between items-center ml-2 mr-1">
                 <label className="text-sm font-bold text-slate-700">Contraseña</label>
                 <a href="#" className="text-xs font-bold text-blue-500 hover:text-blue-600 hover:underline">¿Olvidaste tu contraseña?</a>
               </div>
              <div className="relative group">
                <div className="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
                  <Lock size={18} className="text-slate-400 group-focus-within:text-blue-500 transition-colors" />
                </div>
                <input 
                  type={showPassword ? "text" : "password"} 
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full h-14 bg-slate-50 border border-slate-200 text-slate-600 text-sm rounded-full pl-12 pr-12 outline-none focus:border-blue-400 focus:bg-white focus:ring-4 focus:ring-blue-50 transition-all placeholder:text-slate-300"
                  placeholder="••••••••"
                  required
                />
                <button 
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute inset-y-0 right-0 pr-5 flex items-center text-slate-400 hover:text-slate-600 transition-colors"
                >
                  {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>
            </div>

            {/* Botón Ingresar */}
            <button 
              type="submit"
              className="w-full h-14 bg-gradient-to-r from-blue-500 to-emerald-400 text-white font-bold rounded-full shadow-lg shadow-blue-200 hover:shadow-xl hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2 group mt-4"
            >
              Iniciar Sesión <ArrowRight size={20} className="group-hover:translate-x-1 transition-transform"/>
            </button>

          </form>

          {/* Footer */}
          <div className="mt-auto pt-10 text-center">
            <p className="text-slate-400 text-xs">
              © 2026 Central de Esterilización. Todos los derechos reservados.
            </p>
          </div>

        </div>
      </div>
    </div>
  );
};

export default LoginScreen;