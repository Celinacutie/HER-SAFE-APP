import { useState, useEffect } from "react";

function MyData() {
  const [rows, setRows] = useState([]);
  const [updatingId, setUpdatingId] = useState(null);
  const [updateText, setUpdateText] = useState("");


  
  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem("cases") || "[]");
    setRows(saved);
  }, []);

   const saveUpdate = (id) => {
    const updated = rows.map((row) =>
      row.id === id
        ? { ...row, update: updateText }
        : row
    );
    setRows(updated);
    localStorage.setItem("cases", JSON.stringify(updated));
    setUpdatingId(null);
    setUpdateText("");
};


  return (
    <div style={{ padding: "20px" }}>
      <h2>Your Reported Cases</h2>

      <table border="1" cellPadding="8" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr style={{ backgroundColor: "#f0f0f0" }}>
            <th>ID</th>
            <th>Date</th>
            <th>Case Details</th>
            <th>Description</th>
            <th>Actions Taken</th>
            <th>User Action</th>
          </tr>
        </thead>
        <tbody>
          {rows.length > 0 ? (
            rows.map((row) => (
              <tr key={row.id}>
                <td>{row.id}</td>
                <td>{row.date}</td>
                <td>{row.caseDetails}</td>
                <td>{row.remarks}</td>
                <td>{row.actionsTaken || "Pending"}</td>
                <td>
                  {updatingId === row.id ? (
    <div>
      <textarea
        rows="3"
        placeholder="Describe the new development..."
        value={updateText}
        onChange={(e) => setUpdateText(e.target.value)}
      />
      <br />
      <button onClick={() => saveUpdate(row.id)}>Save</button>
      <button onClick={() => setUpdatingId(null)}>Cancel</button>
    </div>
  ) : (
    <button onClick={() => setUpdatingId(row.id)}>Update</button>
  )}
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="6" style={{ textAlign: "center" }}>
                No cases reported yet.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default MyData;