import React, { useState, useEffect } from 'react';
import { Coffee, Star, ShoppingBag } from 'lucide-react';
import api from './api';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('products/')
      .then(response => {
        setProducts(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Error fetching products:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-orange-50 font-sans">
      <nav className="bg-coffee-900 text-white p-4 shadow-lg sticky top-0 z-50">
        <div className="max-w-md mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Coffee size={24} className="text-orange-300" />
            <h1 className="text-xl font-bold">Dawn & Dusk Café</h1>
          </div>
          <div className="flex items-center gap-4 text-sm">
            <span className="flex items-center gap-1 text-yellow-400">
              <Star size={16} /> 320 Points
            </span>
            <ShoppingBag size={20} />
          </div>
        </div>
      </nav>

      <div className="max-w-md mx-auto p-4 py-8 text-center">
        <h2 className="text-3xl font-bold text-coffee-900 mb-2">Good coffee.<br />Good moments.</h2>
        <p className="text-gray-600 mb-6">Order ahead and earn rewards.</p>
      </div>

      <div className="max-w-md mx-auto p-4 bg-white rounded-t-3xl shadow-xl min-h-screen">
        <h3 className="text-xl font-bold text-gray-800 mb-4">Our Menu</h3>

        {loading ? (
          <p className="text-center text-gray-500 mt-10">Loading freshly brewed menu...</p>
        ) : (
          <div className="grid gap-4">
            {products.map((product) => (
              <div key={product.id} className="flex justify-between items-center p-4 border border-gray-100 rounded-2xl shadow-sm hover:shadow-md transition">
                <div>
                  <h4 className="font-bold text-gray-800">{product.name}</h4>
                  <p className="text-coffee-500 font-semibold">{product.price} EGP</p>
                </div>
                <button className="bg-orange-100 text-orange-600 px-4 py-2 rounded-full font-bold hover:bg-orange-200 transition">
                  Add
                </button>
              </div>
            ))}

            {products.length === 0 && (
              <p className="text-center text-gray-500 mt-10">
                Menu is empty. Add products from Django Admin!
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;