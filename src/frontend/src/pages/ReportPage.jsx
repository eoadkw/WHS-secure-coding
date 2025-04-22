import { useEffect, useState } from "react";
import axios from "axios";

function ReportPage() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/products/reports/", {
        withCredentials: true,
      })
      .then((response) => {
        setReports(response.data);
      })
      .catch((error) => {
        console.error("신고한 상품을 가져오지 못했습니다.", error);
      });
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h2>신고한 상품 목록</h2>
      <ul>
        {reports.map((report) => (
          <li key={report.id}>
            <strong>{report.product_title}</strong> - 사유: {report.reason}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReportPage;

