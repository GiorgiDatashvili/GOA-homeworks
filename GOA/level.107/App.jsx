import React from 'react'


const ResponsiveGrid = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div
        className="
          grid gap-4 w-full max-w-5xl
          grid-cols-1 
          sm:grid-cols-2 sm:grid-rows-2 
          lg:grid-cols-4 lg:grid-rows-1
        "
      >
        <div className="bg-red-400 text-white text-3xl font-bold flex items-center justify-center rounded-lg h-40">
          1
        </div>
        <div className="bg-orange-400 text-white text-3xl font-bold flex items-center justify-center rounded-lg h-40">
          2
        </div>
        <div className="bg-yellow-400 text-white text-3xl font-bold flex items-center justify-center rounded-lg h-40">
          3
        </div>
        <div className="bg-green-400 text-white text-3xl font-bold flex items-center justify-center rounded-lg h-40">
          4
        </div>
      </div>
    </div>
  );
};

export default ResponsiveGrid;
