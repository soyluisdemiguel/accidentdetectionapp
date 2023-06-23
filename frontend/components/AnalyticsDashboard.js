import React, { useEffect, useRef } from 'react';
import { useECharts } from 'react-apache-echarts';
import 'echarts/lib/chart/line';
import 'echarts/lib/component/title';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/legend';

const AnalyticsDashboard = () => {
  const containerRef = useRef(null);
  const echartInstance = useECharts(containerRef);

  useEffect(() => {
    if (echartInstance) {
      const option = {
        title: {
          text: 'Accidents Over Time',
        },
        tooltip: {
          trigger: 'axis',
        },
        legend: {
          data: ['Accidents'],
        },
        xAxis: {
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        },
        yAxis: {},
        series: [
          {
            name: 'Accidents',
            type: 'line',
            data: [120, 200, 150, 80, 70, 110, 130],
          },
        ],
      };

      echartInstance.setOption(option);
    }
  }, [echartInstance]);

  return (
    <div
      ref={containerRef}
      style={{
        width: '100%',
        height: '400px',
      }}
    />
  );
};

export default AnalyticsDashboard;
