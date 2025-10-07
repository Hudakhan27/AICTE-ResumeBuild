import React from "react";

function Portfolio({ data }) {
  return (
    <div className="p-6 bg-gray-50">
      <h1 className="text-4xl font-bold">{data.name}</h1>
      <p className="text-gray-600">{data.email}</p>
      <h2 className="text-2xl mt-4 font-semibold">Skills</h2>
      <p>{data.skills}</p>
      <h2 className="text-2xl mt-4 font-semibold">Education</h2>
      <p>{data.education}</p>
      <h2 className="text-2xl mt-4 font-semibold">Projects</h2>
      <p>{data.projects}</p>
    </div>
  );
}

export default Portfolio;
