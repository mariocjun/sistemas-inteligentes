import os
import subprocess
import fitz

EDGE_PATH = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Guia Didático Visual de Escalonamento - Prof. Carlos Maziero</title>
<style>
    @page {
        size: A4 portrait;
        margin: 6mm 7mm;
    }
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #0f172a;
        background: #fff;
        font-size: 7.5pt;
        line-height: 1.3;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    .page {
        page-break-after: always;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .page:last-child {
        page-break-after: auto;
    }
    .header-banner {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #fff;
        padding: 2.5mm 4mm;
        border-radius: 2mm;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 3mm;
    }
    .header-title {
        font-size: 10.5pt;
        font-weight: 800;
    }
    .header-badge {
        background: #2563eb;
        color: #fff;
        padding: 0.8mm 2.2mm;
        border-radius: 1mm;
        font-size: 7.5pt;
        font-weight: 700;
        margin-right: 2mm;
    }
    .header-sub {
        font-size: 6.8pt;
        color: #94a3b8;
    }

    .section-title {
        font-size: 9pt;
        font-weight: 800;
        color: #1e293b;
        margin-top: 2.5mm;
        margin-bottom: 1.5mm;
        display: flex;
        align-items: center;
        gap: 2mm;
        border-bottom: 1.2px solid #e2e8f0;
        padding-bottom: 0.8mm;
    }
    .algo-badge {
        background: #0284c7;
        color: #fff;
        padding: 0.5mm 1.8mm;
        border-radius: 0.8mm;
        font-size: 7pt;
    }

    /* CARD DESIGN */
    .card {
        border: 0.7px solid #cbd5e1;
        border-radius: 1.8mm;
        background: #fff;
        margin-bottom: 2.5mm;
        overflow: hidden;
    }
    .card-header {
        background: #f8fafc;
        border-bottom: 0.7px solid #e2e8f0;
        padding: 1.2mm 2.5mm;
        font-weight: 700;
        font-size: 7.5pt;
        color: #334155;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .card-body {
        padding: 2mm 2.5mm;
    }

    /* GANTT DIAGRAM STYLE (MAZIERO STYLE) */
    .gantt-chart {
        width: 100%;
        margin: 1.5mm 0;
        background: #fafafa;
        border: 0.6px solid #e2e8f0;
        border-radius: 1.2mm;
        padding: 2mm 3mm;
    }
    .gantt-row {
        display: flex;
        align-items: center;
        height: 5.2mm;
        margin-bottom: 1mm;
        position: relative;
    }
    .task-label {
        width: 7mm;
        font-weight: 800;
        font-size: 7.5pt;
        color: #334155;
    }
    .gantt-track {
        flex: 1;
        height: 100%;
        display: flex;
        position: relative;
        background: #fff;
        border-left: 1px solid #64748b;
        border-bottom: 1px solid #64748b;
    }
    .grid-lines {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        display: flex;
        pointer-events: none;
    }
    .grid-col {
        flex: 1;
        border-right: 0.5px dashed #e2e8f0;
        height: 100%;
    }
    .grid-col:last-child {
        border-right: none;
    }
    
    /* SEGMENTS */
    .box {
        position: absolute;
        top: 0.6mm;
        bottom: 0.6mm;
        border-radius: 0.6mm;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 6pt;
        font-weight: 700;
        border: 0.6px solid #000;
    }
    .box-wait {
        background: #ffffff;
        color: #475569;
        border: 0.6px solid #64748b;
    }
    .box-t1 { background: #2563eb; color: #fff; }
    .box-t2 { background: #eab308; color: #000; }
    .box-t3 { background: #9333ea; color: #fff; }
    .box-t4 { background: #16a34a; color: #fff; }
    .box-t5 { background: #dc2626; color: #fff; }

    /* SCALE TICKS */
    .gantt-axis {
        display: flex;
        margin-left: 7mm;
        height: 4mm;
        align-items: flex-start;
        border-top: 1px solid #64748b;
    }
    .axis-tick {
        flex: 1;
        font-size: 6pt;
        color: #64748b;
        text-align: left;
        padding-top: 0.6mm;
        position: relative;
    }
    .axis-tick::before {
        content: "";
        position: absolute;
        top: -1px;
        left: 0;
        width: 1px;
        height: 1.5mm;
        background: #64748b;
    }
    .axis-tick-end {
        width: 0;
        position: relative;
        font-size: 6pt;
        color: #64748b;
        padding-top: 0.6mm;
    }
    .axis-tick-end::before {
        content: "";
        position: absolute;
        top: -1px;
        left: 0;
        width: 1px;
        height: 1.5mm;
        background: #64748b;
    }

    .didactic-steps {
        background: #eff6ff;
        border-left: 2.5px solid #3b82f6;
        padding: 1.5mm 2.5mm;
        border-radius: 0 1.2mm 1.2mm 0;
        font-size: 6.8pt;
        margin-top: 1.5mm;
    }
    .didactic-steps ol {
        margin-left: 3.5mm;
        margin-top: 0.8mm;
    }
    .didactic-steps li {
        margin-bottom: 0.6mm;
    }
    .metrics-tag {
        font-size: 6.8pt;
        background: #f1f5f9;
        padding: 0.5mm 1.8mm;
        border-radius: 0.8mm;
        font-weight: 700;
        color: #0f172a;
        border: 0.5px solid #cbd5e1;
    }

    /* RR STEP TABLE */
    .rr-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 6.2pt;
        margin-top: 1.5mm;
    }
    .rr-table th, .rr-table td {
        border: 0.5px solid #cbd5e1;
        padding: 0.8mm 1.2mm;
        text-align: center;
    }
    .rr-table th {
        background: #1e293b;
        color: #fff;
    }
    .rr-table tr:nth-child(even) {
        background: #f8fafc;
    }
    .queue-box {
        font-family: monospace;
        background: #f1f5f9;
        padding: 0.3mm 1mm;
        border-radius: 0.5mm;
        border: 0.5px solid #cbd5e1;
        font-weight: 700;
    }
</style>
</head>
<body>

<!-- ================= PÁGINA 1 ================= -->
<div class="page">
    <div class="header-banner">
        <div>
            <span class="header-badge">UFPR / SOCM</span>
            <span class="header-title">Guia Visual Didático dos Escalonadores de CPU (Capítulo 06)</span>
        </div>
        <div class="header-sub">Prof. Carlos Maziero • Reprodução dos Diagramas Oficiais do Livro/Slides</div>
    </div>

    <!-- TABELA CANONICA DE TAREFAS -->
    <div class="card" style="margin-bottom: 2mm;">
        <div class="card-header">
            <span>📌 O Exemplo Canônico Geral do Capítulo 06 (Utilizado em todos os algoritmos)</span>
            <span style="font-weight: normal; font-size: 6.5pt;">Convenção: Maior número = Maior prioridade</span>
        </div>
        <div class="card-body" style="padding: 1.5mm 2.5mm;">
            <div style="display: flex; gap: 3mm; align-items: center;">
                <div style="flex: 1.5;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 6.5pt; text-align: center;">
                        <tr style="background: #f1f5f9; font-weight: bold;">
                            <td style="border: 0.5px solid #cbd5e1; padding: 0.8mm;">Tarefa</td>
                            <td style="border: 0.5px solid #cbd5e1; color: #2563eb;">t1</td>
                            <td style="border: 0.5px solid #cbd5e1; color: #d97706;">t2</td>
                            <td style="border: 0.5px solid #cbd5e1; color: #9333ea;">t3</td>
                            <td style="border: 0.5px solid #cbd5e1; color: #16a34a;">t4</td>
                            <td style="border: 0.5px solid #cbd5e1; color: #dc2626;">t5</td>
                        </tr>
                        <tr>
                            <td style="border: 0.5px solid #cbd5e1; font-weight: bold; background: #f8fafc;">Ingresso (s)</td>
                            <td style="border: 0.5px solid #cbd5e1;">0</td>
                            <td style="border: 0.5px solid #cbd5e1;">0</td>
                            <td style="border: 0.5px solid #cbd5e1;">1</td>
                            <td style="border: 0.5px solid #cbd5e1;">3</td>
                            <td style="border: 0.5px solid #cbd5e1;">5</td>
                        </tr>
                        <tr>
                            <td style="border: 0.5px solid #cbd5e1; font-weight: bold; background: #f8fafc;">Duração (s)</td>
                            <td style="border: 0.5px solid #cbd5e1;">5</td>
                            <td style="border: 0.5px solid #cbd5e1;">2</td>
                            <td style="border: 0.5px solid #cbd5e1;">4</td>
                            <td style="border: 0.5px solid #cbd5e1;">1</td>
                            <td style="border: 0.5px solid #cbd5e1;">2</td>
                        </tr>
                        <tr>
                            <td style="border: 0.5px solid #cbd5e1; font-weight: bold; background: #f8fafc;">Prioridade</td>
                            <td style="border: 0.5px solid #cbd5e1;">2</td>
                            <td style="border: 0.5px solid #cbd5e1;">3</td>
                            <td style="border: 0.5px solid #cbd5e1;">1</td>
                            <td style="border: 0.5px solid #cbd5e1;">4</td>
                            <td style="border: 0.5px solid #cbd5e1;">5</td>
                        </tr>
                    </table>
                </div>
                <div style="flex: 1; font-size: 6.2pt; border-left: 1px solid #e2e8f0; padding-left: 2mm;">
                    <strong>Legenda Visual do Maziero:</strong><br>
                    • <span style="display:inline-block; width: 3mm; height: 2mm; background: #fff; border: 0.5px solid #64748b;"></span> <strong>Caixa Branca:</strong> Tempo de espera ($t_w$) na fila de prontos.<br>
                    • <span style="display:inline-block; width: 3mm; height: 2mm; background: #2563eb;"></span> <strong>Caixa Colorida:</strong> Execução ativa na CPU.<br>
                    • Fórmulas: $t_t = f_i - c_i$ | $t_w = t_t - d_i$.
                </div>
            </div>
        </div>
    </div>

    <!-- 1. FCFS -->
    <div class="card">
        <div class="card-header">
            <span>1. Escalonamento FCFS (First Come, First Served)</span>
            <span class="metrics-tag">Tt = 8,0 s | Tw = 5,2 s | 4 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <!-- t5 -->
                <div class="gantt-row">
                    <div class="task-label">t5</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 5/14); width: calc(100% * 7/14);">Espera [5 a 12] (7s)</div>
                        <div class="box box-t5" style="left: calc(100% * 12/14); width: calc(100% * 2/14);">CPU (2s)</div>
                    </div>
                </div>
                <!-- t4 -->
                <div class="gantt-row">
                    <div class="task-label">t4</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 3/14); width: calc(100% * 8/14);">Espera [3 a 11] (8s)</div>
                        <div class="box box-t4" style="left: calc(100% * 11/14); width: calc(100% * 1/14);">CPU</div>
                    </div>
                </div>
                <!-- t3 -->
                <div class="gantt-row">
                    <div class="task-label">t3</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 1/14); width: calc(100% * 6/14);">Espera [1 a 7] (6s)</div>
                        <div class="box box-t3" style="left: calc(100% * 7/14); width: calc(100% * 4/14);">CPU [7 a 11] (4s)</div>
                    </div>
                </div>
                <!-- t2 -->
                <div class="gantt-row">
                    <div class="task-label">t2</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: 0; width: calc(100% * 5/14);">Espera [0 a 5] (5s)</div>
                        <div class="box box-t2" style="left: calc(100% * 5/14); width: calc(100% * 2/14);">CPU (2s)</div>
                    </div>
                </div>
                <!-- t1 -->
                <div class="gantt-row">
                    <div class="task-label">t1</div>
                    <div class="gantt-track">
                        <div class="box box-t1" style="left: 0; width: calc(100% * 5/14);">CPU [0 a 5] (5s)</div>
                    </div>
                </div>
                <!-- Axis -->
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div>
                    <div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div>
                    <div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-steps">
                <strong>Como desenhar passo a passo (Lógica FCFS):</strong>
                <ol>
                    <li>Ordene estritamente pela chegada (c<sub>i</sub>): t<sub>1</sub>(0) &rarr; t<sub>2</sub>(0) &rarr; t<sub>3</sub>(1) &rarr; t<sub>4</sub>(3) &rarr; t<sub>5</sub>(5). Desempate t<sub>1</sub>/t<sub>2</sub> pelo índice.</li>
                    <li>Desenhe t<sub>1</sub> de 0 a 5 na CPU. Durante esse tempo, t<sub>2</sub> espera (caixa branca de 0 a 5).</li>
                    <li>Terminou t<sub>1</sub>? Chame o próximo da fila (t<sub>2</sub>): pinta de 5 a 7. O próximo (t<sub>3</sub>) esperou de 1 a 7 e roda de 7 a 11.</li>
                    <li>Cada tarefa roda até o fim sem interrupções. t<sub>4</sub> roda [11-12] e t<sub>5</sub> roda [12-14].</li>
                </ol>
            </div>
        </div>
    </div>

    <!-- 2. SJF -->
    <div class="card">
        <div class="card-header">
            <span>2. Escalonamento SJF (Shortest Job First - Cooperativo)</span>
            <span class="metrics-tag">Tt = 5,8 s | Tw = 3,0 s | 4 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <!-- t5 -->
                <div class="gantt-row">
                    <div class="task-label">t5</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 5/14); width: calc(100% * 2/14);">Espera (2s)</div>
                        <div class="box box-t5" style="left: calc(100% * 7/14); width: calc(100% * 2/14);">CPU [7 a 9]</div>
                    </div>
                </div>
                <!-- t4 -->
                <div class="gantt-row">
                    <div class="task-label">t4</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 3/14); width: calc(100% * 3/14);">Espera (3s)</div>
                        <div class="box box-t4" style="left: calc(100% * 6/14); width: calc(100% * 1/14);">CPU</div>
                    </div>
                </div>
                <!-- t3 -->
                <div class="gantt-row">
                    <div class="task-label">t3</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 1/14); width: calc(100% * 1/14);">Esp</div>
                        <div class="box box-t3" style="left: calc(100% * 2/14); width: calc(100% * 4/14);">CPU [2 a 6] (4s)</div>
                    </div>
                </div>
                <!-- t2 -->
                <div class="gantt-row">
                    <div class="task-label">t2</div>
                    <div class="gantt-track">
                        <div class="box box-t2" style="left: 0; width: calc(100% * 2/14);">CPU [0 a 2]</div>
                    </div>
                </div>
                <!-- t1 -->
                <div class="gantt-row">
                    <div class="task-label">t1</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: 0; width: calc(100% * 9/14);">Espera [0 a 9] (9s)</div>
                        <div class="box box-t1" style="left: calc(100% * 9/14); width: calc(100% * 5/14);">CPU [9 a 14] (5s)</div>
                    </div>
                </div>
                <!-- Axis -->
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div>
                    <div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div>
                    <div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-steps">
                <strong>Como desenhar passo a passo (Decisões em cada término):</strong>
                <ol>
                    <li>Em t = 0, prontas {t<sub>1</sub>(d=5), t<sub>2</sub>(d=2)}. Menor duração d é t<sub>2</sub>. Pinte t<sub>2</sub> de 0 a 2.</li>
                    <li>Em t = 2, prontas {t<sub>1</sub>(5), t<sub>3</sub>(4)}. Menor duração d é t<sub>3</sub>. Pinte t<sub>3</sub> de 2 a 6.</li>
                    <li>Em t = 6, prontas {t<sub>1</sub>(5), t<sub>4</sub>(1), t<sub>5</sub>(2)}. Menor d é t<sub>4</sub>. Pinte t<sub>4</sub> de 6 a 7.</li>
                    <li>Em t = 7, prontas {t<sub>1</sub>(5), t<sub>5</sub>(2)}. Menor d é t<sub>5</sub>. Pinte t<sub>5</sub> de 7 a 9. Por fim, t<sub>1</sub> roda de 9 a 14.</li>
                </ol>
            </div>
        </div>
    </div>
</div>

<!-- ================= PÁGINA 2 ================= -->
<div class="page">
    <div class="header-banner">
        <div>
            <span class="header-badge">UFPR / SOCM</span>
            <span class="header-title">Escalonadores Preemptivos: SRTF e Round-Robin (Capítulo 06)</span>
        </div>
        <div class="header-sub">Preempção por Menor Restante e por Quantum de Tempo</div>
    </div>

    <!-- 3. SRTF -->
    <div class="card">
        <div class="card-header">
            <span>3. Escalonamento SRTF (Shortest Remaining Time First - Preemptivo)</span>
            <span class="metrics-tag">Tt = 5,4 s | Tw = 2,6 s | 5 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <!-- t5 -->
                <div class="gantt-row">
                    <div class="task-label">t5</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 5/14); width: calc(100% * 2/14);">Espera</div>
                        <div class="box box-t5" style="left: calc(100% * 7/14); width: calc(100% * 2/14);">CPU [7 a 9]</div>
                    </div>
                </div>
                <!-- t4 -->
                <div class="gantt-row">
                    <div class="task-label">t4</div>
                    <div class="gantt-track">
                        <div class="box box-t4" style="left: calc(100% * 3/14); width: calc(100% * 1/14);">CPU [3-4]</div>
                    </div>
                </div>
                <!-- t3 -->
                <div class="gantt-row">
                    <div class="task-label">t3</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 1/14); width: calc(100% * 1/14);">Esp</div>
                        <div class="box box-t3" style="left: calc(100% * 2/14); width: calc(100% * 1/14);">CPU</div>
                        <div class="box box-wait" style="left: calc(100% * 3/14); width: calc(100% * 1/14);">Preemptada</div>
                        <div class="box box-t3" style="left: calc(100% * 4/14); width: calc(100% * 3/14);">CPU [4 a 7] (3s)</div>
                    </div>
                </div>
                <!-- t2 -->
                <div class="gantt-row">
                    <div class="task-label">t2</div>
                    <div class="gantt-track">
                        <div class="box box-t2" style="left: 0; width: calc(100% * 2/14);">CPU [0 a 2]</div>
                    </div>
                </div>
                <!-- t1 -->
                <div class="gantt-row">
                    <div class="task-label">t1</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: 0; width: calc(100% * 9/14);">Espera [0 a 9] (9s)</div>
                        <div class="box box-t1" style="left: calc(100% * 9/14); width: calc(100% * 5/14);">CPU [9 a 14] (5s)</div>
                    </div>
                </div>
                <!-- Axis -->
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div>
                    <div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div>
                    <div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-steps">
                <strong>O ponto-chave do desenho (A Preempção em t = 3):</strong>
                <ol>
                    <li>Em t = 2, t<sub>3</sub>(d=4) começa a rodar. Em t = 3, chega t<sub>4</sub> com duração 1. Como resta 3 s de t<sub>3</sub> e 1 &lt; 3, <strong>t<sub>4</sub> preempta t<sub>3</sub>!</strong></li>
                    <li>No desenho, <strong>interrompa a barra colorida de t<sub>3</sub> em 3</strong>, desenhe uma caixa branca de espera em [3 a 4], e pinte a caixa de t<sub>4</sub> em [3 a 4].</li>
                    <li>Quando t<sub>4</sub> conclui em 4, t<sub>3</sub> retoma a CPU e termina em 7.</li>
                </ol>
            </div>
        </div>
    </div>

    <!-- 4. ROUND-ROBIN (SLIDE 11 COMPLETO) -->
    <div class="card">
        <div class="card-header">
            <span>4. Escalonamento Round-Robin (Revezamento com Quantum tq = 2) — O Slide 11 Passo a Passo</span>
            <span class="metrics-tag">Tt = 8,4 s | Tw = 5,6 s | 7 Trocas</span>
        </div>
        <div class="card-body">
            <!-- GANTT DO RR -->
            <div class="gantt-chart" style="margin-bottom: 2mm;">
                <!-- t5 -->
                <div class="gantt-row">
                    <div class="task-label">t5</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 5/14); width: calc(100% * 4/14);">Espera</div>
                        <div class="box box-t5" style="left: calc(100% * 9/14); width: calc(100% * 2/14);">CPU [9-11]</div>
                    </div>
                </div>
                <!-- t4 -->
                <div class="gantt-row">
                    <div class="task-label">t4</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 3/14); width: calc(100% * 5/14);">Espera (5s)</div>
                        <div class="box box-t4" style="left: calc(100% * 8/14); width: calc(100% * 1/14);">CPU</div>
                    </div>
                </div>
                <!-- t3 -->
                <div class="gantt-row">
                    <div class="task-label">t3</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 1/14); width: calc(100% * 3/14);">Espera</div>
                        <div class="box box-t3" style="left: calc(100% * 4/14); width: calc(100% * 2/14);">CPU [4-6]</div>
                        <div class="box box-wait" style="left: calc(100% * 6/14); width: calc(100% * 5/14);">Espera (5s)</div>
                        <div class="box box-t3" style="left: calc(100% * 11/14); width: calc(100% * 2/14);">CPU [11-13]</div>
                    </div>
                </div>
                <!-- t2 -->
                <div class="gantt-row">
                    <div class="task-label">t2</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: 0; width: calc(100% * 2/14);">Esp</div>
                        <div class="box box-t2" style="left: calc(100% * 2/14); width: calc(100% * 2/14);">CPU [2 a 4]</div>
                    </div>
                </div>
                <!-- t1 -->
                <div class="gantt-row">
                    <div class="task-label">t1</div>
                    <div class="gantt-track">
                        <div class="box box-t1" style="left: 0; width: calc(100% * 2/14);">CPU [0-2]</div>
                        <div class="box box-wait" style="left: calc(100% * 2/14); width: calc(100% * 4/14);">Espera</div>
                        <div class="box box-t1" style="left: calc(100% * 6/14); width: calc(100% * 2/14);">CPU [6-8]</div>
                        <div class="box box-wait" style="left: calc(100% * 8/14); width: calc(100% * 5/14);">Espera</div>
                        <div class="box box-t1" style="left: calc(100% * 13/14); width: calc(100% * 1/14);">CPU</div>
                    </div>
                </div>
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div>
                    <div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div>
                    <div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>

            <!-- TABELA DO SLIDE 11 (FILA SEGUNDO A SEGUNDO) -->
            <table class="rr-table">
                <thead>
                    <tr>
                        <th style="width: 8mm;">Tempo</th>
                        <th style="width: 14mm;">Fila Prontos</th>
                        <th style="width: 10mm;">CPU</th>
                        <th>Evento / Regra Didática de Transição</th>
                        <th style="width: 8mm;">Tempo</th>
                        <th style="width: 14mm;">Fila Prontos</th>
                        <th style="width: 10mm;">CPU</th>
                        <th>Evento / Regra Didática de Transição</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>t = 0</strong></td><td><span class="queue-box">[ t2 ]</span></td><td><span class="box-t1" style="padding:0.2mm 1mm;">t1</span></td><td>t1 entra na CPU; t2 aguarda na fila</td>
                        <td><strong>t = 8</strong></td><td><span class="queue-box">[ t1, t3, t5 ]</span></td><td><span class="box-t4" style="padding:0.2mm 1mm;">t4</span></td><td>t4 roda; precisa só de 1 s (termina em 9)</td>
                    </tr>
                    <tr>
                        <td><strong>t = 1</strong></td><td><span class="queue-box">[ t3, t2 ]</span></td><td><span class="box-t1" style="padding:0.2mm 1mm;">t1</span></td><td>t3 chega e entra no fim da fila</td>
                        <td><strong>t = 9</strong></td><td><span class="queue-box">[ t1, t3 ]</span></td><td><span class="box-t5" style="padding:0.2mm 1mm;">t5</span></td><td>t4 termina (FIM); t5 assume a CPU</td>
                    </tr>
                    <tr>
                        <td><strong>t = 2</strong></td><td><span class="queue-box">[ t1, t3 ]</span></td><td><span class="box-t2" style="padding:0.2mm 1mm;">t2</span></td><td>Fim do quantum de t1 (volta à fila); t2 assume</td>
                        <td><strong>t = 10</strong></td><td><span class="queue-box">[ t1, t3 ]</span></td><td><span class="box-t5" style="padding:0.2mm 1mm;">t5</span></td><td>t5 completa seu 2º segundo de quantum</td>
                    </tr>
                    <tr>
                        <td><strong>t = 3</strong></td><td><span class="queue-box">[ t4, t1, t3 ]</span></td><td><span class="box-t2" style="padding:0.2mm 1mm;">t2</span></td><td>t4 chega e entra no fim da fila</td>
                        <td><strong>t = 11</strong></td><td><span class="queue-box">[ t1 ]</span></td><td><span class="box-t3" style="padding:0.2mm 1mm;">t3</span></td><td>t5 termina (FIM); t3 assume a CPU</td>
                    </tr>
                    <tr>
                        <td><strong>t = 4</strong></td><td><span class="queue-box">[ t4, t1 ]</span></td><td><span class="box-t3" style="padding:0.2mm 1mm;">t3</span></td><td>t2 termina (FIM); t3 assume a CPU</td>
                        <td><strong>t = 12</strong></td><td><span class="queue-box">[ t1 ]</span></td><td><span class="box-t3" style="padding:0.2mm 1mm;">t3</span></td><td>t3 completa seu 2º segundo de quantum</td>
                    </tr>
                    <tr>
                        <td><strong>t = 5</strong></td><td><span class="queue-box">[ t5, t4, t1 ]</span></td><td><span class="box-t3" style="padding:0.2mm 1mm;">t3</span></td><td>t5 chega e entra no fim da fila</td>
                        <td><strong>t = 13</strong></td><td><span class="queue-box">[ vazio ]</span></td><td><span class="box-t1" style="padding:0.2mm 1mm;">t1</span></td><td>t3 termina (FIM); t1 roda seu 1 s restante</td>
                    </tr>
                    <tr>
                        <td><strong>t = 6</strong></td><td><span class="queue-box">[ t3, t5, t4 ]</span></td><td><span class="box-t1" style="padding:0.2mm 1mm;">t1</span></td><td>Fim do quantum de t3; t1 assume a CPU</td>
                        <td><strong>t = 14</strong></td><td><span class="queue-box">[ vazio ]</span></td><td>—</td><td>t1 termina (FIM). Todas concluídas!</td>
                    </tr>
                    <tr>
                        <td><strong>t = 7</strong></td><td><span class="queue-box">[ t3, t5, t4 ]</span></td><td><span class="box-t1" style="padding:0.2mm 1mm;">t1</span></td><td>t1 completa seu 2º segundo na CPU</td>
                        <td colspan="4" style="background:#f1f5f9; font-weight:bold; color:#1e40af;">Regra: Chegadas novas entram ANTES de quem sofre preempção!</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- ================= PÁGINA 3 ================= -->
<div class="page">
    <div class="header-banner">
        <div>
            <span class="header-badge">UFPR / SOCM</span>
            <span class="header-title">Escalonadores por Prioridade & Quadro Comparativo (Capítulo 06)</span>
        </div>
        <div class="header-sub">PRIOc, PRIOp, PRIOd (Aging) e Comparação Geral das Métricas</div>
    </div>

    <!-- 5. PRIOc e PRIOp LADO A LADO -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm; margin-bottom: 2mm;">
        <!-- PRIOc -->
        <div class="card">
            <div class="card-header">
                <span>5. PRIOc (Prioridade Cooperativa)</span>
                <span class="metrics-tag">Tt = 6,6 s | Tw = 3,8 s</span>
            </div>
            <div class="card-body">
                <div class="gantt-chart">
                    <div class="gantt-row"><div class="task-label">t5</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">Esp</div><div class="box box-t5" style="left:calc(100%*7/14); width:calc(100%*2/14);">CPU [7-9]</div></div></div>
                    <div class="gantt-row"><div class="task-label">t4</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*6/14);">Espera</div><div class="box box-t4" style="left:calc(100%*9/14); width:calc(100%*1/14);">CPU</div></div></div>
                    <div class="gantt-row"><div class="task-label">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*9/14);">Espera [1 a 10]</div><div class="box box-t3" style="left:calc(100%*10/14); width:calc(100%*4/14);">CPU</div></div></div>
                    <div class="gantt-row"><div class="task-label">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*2/14);">CPU [0-2]</div></div></div>
                    <div class="gantt-row"><div class="task-label">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*2/14);">Esp</div><div class="box box-t1" style="left:calc(100%*2/14); width:calc(100%*5/14);">CPU [2 a 7]</div></div></div>
                    <div class="gantt-axis"><div class="axis-tick">0</div><div class="axis-tick">2</div><div class="axis-tick">7</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick-end">14</div></div>
                </div>
                <div style="font-size: 6.2pt; color: #475569; margin-top: 1mm;">
                    <strong>Ordem de Execução:</strong> t<sub>2</sub>(p=3) &rarr; t<sub>1</sub>(p=2) &rarr; t<sub>5</sub>(p=5) &rarr; t<sub>4</sub>(p=4) &rarr; t<sub>3</sub>(p=1). Como é cooperativo, ninguém interrompe t<sub>1</sub> em 3 ou 5.
                </div>
            </div>
        </div>

        <!-- PRIOp -->
        <div class="card">
            <div class="card-header">
                <span>6. PRIOp (Prioridade Preemptiva)</span>
                <span class="metrics-tag">Tt = 5,6 s | Tw = 2,8 s</span>
            </div>
            <div class="card-body">
                <div class="gantt-chart">
                    <div class="gantt-row"><div class="task-label">t5</div><div class="gantt-track"><div class="box box-t5" style="left:calc(100%*5/14); width:calc(100%*2/14);">CPU [5-7]</div></div></div>
                    <div class="gantt-row"><div class="task-label">t4</div><div class="gantt-track"><div class="box box-t4" style="left:calc(100%*3/14); width:calc(100%*1/14);">CPU [3-4]</div></div></div>
                    <div class="gantt-row"><div class="task-label">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*9/14);">Espera [1 a 10]</div><div class="box box-t3" style="left:calc(100%*10/14); width:calc(100%*4/14);">CPU</div></div></div>
                    <div class="gantt-row"><div class="task-label">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*2/14);">CPU [0-2]</div></div></div>
                    <div class="gantt-row"><div class="task-label">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*2/14);">Esp</div><div class="box box-t1" style="left:calc(100%*2/14); width:calc(100%*1/14);">1s</div><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*1/14);">P</div><div class="box box-t1" style="left:calc(100%*4/14); width:calc(100%*1/14);">1s</div><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">P</div><div class="box box-t1" style="left:calc(100%*7/14); width:calc(100%*3/14);">3s [7-10]</div></div></div>
                    <div class="gantt-axis"><div class="axis-tick">0</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">5</div><div class="axis-tick">7</div><div class="axis-tick">10</div><div class="axis-tick-end">14</div></div>
                </div>
                <div style="font-size: 6.2pt; color: #475569; margin-top: 1mm;">
                    <strong>Duas Preempções em t<sub>1</sub>:</strong> Em t = 3 por t<sub>4</sub>(p=4) e em t = 5 por t<sub>5</sub>(p=5). A barra de t<sub>1</sub> é fatiada em 3 blocos: [2-3], [4-5] e [7-10]!
                </div>
            </div>
        </div>
    </div>

    <!-- 7. PRIOd (AGING) -->
    <div class="card">
        <div class="card-header">
            <span>7. Escalonamento PRIOd (Prioridades Dinâmicas com Envelhecimento / Aging, &alpha; = 1) — Slide 23</span>
            <span class="metrics-tag">Tt = 5,8 s | Tw = 3,0 s | 6 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <!-- t5 -->
                <div class="gantt-row">
                    <div class="task-label">t5</div>
                    <div class="gantt-track">
                        <div class="box box-t5" style="left: calc(100% * 5/14); width: calc(100% * 2/14);">5 (CPU [5-7])</div>
                    </div>
                </div>
                <!-- t4 -->
                <div class="gantt-row">
                    <div class="task-label">t4</div>
                    <div class="gantt-track">
                        <div class="box box-t4" style="left: calc(100% * 3/14); width: calc(100% * 1/14);">4 (CPU [3-4])</div>
                    </div>
                </div>
                <!-- t3 -->
                <div class="gantt-row">
                    <div class="task-label">t3</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: calc(100% * 1/14); width: calc(100% * 1/14);">2</div>
                        <div class="box box-wait" style="left: calc(100% * 2/14); width: calc(100% * 1/14);">3</div>
                        <div class="box box-wait" style="left: calc(100% * 3/14); width: calc(100% * 1/14);">4</div>
                        <div class="box box-t3" style="left: calc(100% * 4/14); width: calc(100% * 1/14);">1 (CPU)</div>
                        <div class="box box-wait" style="left: calc(100% * 5/14); width: calc(100% * 1/14);">2</div>
                        <div class="box box-wait" style="left: calc(100% * 6/14); width: calc(100% * 1/14);">3</div>
                        <div class="box box-wait" style="left: calc(100% * 7/14); width: calc(100% * 4/14);">... sobe ...</div>
                        <div class="box box-t3" style="left: calc(100% * 11/14); width: calc(100% * 3/14);">1 (CPU [11 a 14])</div>
                    </div>
                </div>
                <!-- t2 -->
                <div class="gantt-row">
                    <div class="task-label">t2</div>
                    <div class="gantt-track">
                        <div class="box box-t2" style="left: 0; width: calc(100% * 1/14);">3</div>
                        <div class="box box-t2" style="left: calc(100% * 1/14); width: calc(100% * 1/14);">3</div>
                    </div>
                </div>
                <!-- t1 -->
                <div class="gantt-row">
                    <div class="task-label">t1</div>
                    <div class="gantt-track">
                        <div class="box box-wait" style="left: 0; width: calc(100% * 1/14);">3</div>
                        <div class="box box-wait" style="left: calc(100% * 1/14); width: calc(100% * 1/14);">4</div>
                        <div class="box box-t1" style="left: calc(100% * 2/14); width: calc(100% * 1/14);">2 (CPU)</div>
                        <div class="box box-wait" style="left: calc(100% * 3/14); width: calc(100% * 1/14);">3</div>
                        <div class="box box-wait" style="left: calc(100% * 4/14); width: calc(100% * 1/14);">4</div>
                        <div class="box box-wait" style="left: calc(100% * 5/14); width: calc(100% * 1/14);">5</div>
                        <div class="box box-wait" style="left: calc(100% * 6/14); width: calc(100% * 1/14);">6</div>
                        <div class="box box-t1" style="left: calc(100% * 7/14); width: calc(100% * 4/14);">2 (CPU [7 a 11])</div>
                    </div>
                </div>
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div>
                    <div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div>
                    <div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-steps">
                <strong>O que representam os números dentro das caixinhas (Slide 23)?</strong>
                São os valores da <strong>prioridade dinâmica (pd)</strong> em cada segundo:
                <br>• Se a tarefa <em>espera</em> na fila, sua prioridade aumenta: <strong>pd &larr; pd + 1</strong>.
                <br>• Se a tarefa <em>executa</em> na CPU, sua prioridade é resetada para o valor estático original: <strong>pd &larr; pe</strong>.
                <br>• Em t = 4, t<sub>3</sub> acumulou pd = 4 e desempata com t<sub>1</sub>(pd=4) no critério estático, ganhando a CPU!
            </div>
        </div>
    </div>

    <!-- QUADRO COMPARATIVO OFICIAL (SLIDE 26) -->
    <div class="card">
        <div class="card-header">
            <span>📊 Quadro Comparativo Oficial de Todos os Algoritmos (Slide 26)</span>
            <span style="font-weight: normal; font-size: 6.5pt;">Gabarito Teórico Completo do Capítulo 06</span>
        </div>
        <div class="card-body">
            <table style="width: 100%; border-collapse: collapse; font-size: 6.8pt; text-align: center;">
                <tr style="background: #1e293b; color: #fff; font-weight: bold;">
                    <td style="padding: 1.2mm; border: 0.5px solid #475569;">Métrica</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569;">FCFS</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569; color: #f87171;">RR (q=2)</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569;">SJF</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569; color: #60a5fa;">SRTF</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569;">PRIOc</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569;">PRIOp</td>
                    <td style="padding: 1.2mm; border: 0.5px solid #475569;">PRIOd</td>
                </tr>
                <tr>
                    <td style="font-weight: bold; background: #f8fafc; border: 0.5px solid #cbd5e1; text-align: left; padding-left: 2mm;">Tempo médio de retorno (Tt)</td>
                    <td style="border: 0.5px solid #cbd5e1;">8,0 s</td>
                    <td style="border: 0.5px solid #cbd5e1; font-weight: bold;">8,4 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">5,8 s</td>
                    <td style="border: 0.5px solid #cbd5e1; font-weight: bold; background: #dbeafe; color: #1e40af;">5,4 s (Mínimo)</td>
                    <td style="border: 0.5px solid #cbd5e1;">6,6 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">5,6 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">5,8 s</td>
                </tr>
                <tr>
                    <td style="font-weight: bold; background: #f8fafc; border: 0.5px solid #cbd5e1; text-align: left; padding-left: 2mm;">Tempo médio de espera (Tw)</td>
                    <td style="border: 0.5px solid #cbd5e1;">5,2 s</td>
                    <td style="border: 0.5px solid #cbd5e1; font-weight: bold;">5,6 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">3,0 s</td>
                    <td style="border: 0.5px solid #cbd5e1; font-weight: bold; background: #dbeafe; color: #1e40af;">2,6 s (Mínimo)</td>
                    <td style="border: 0.5px solid #cbd5e1;">3,8 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">2,8 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">3,0 s</td>
                </tr>
                <tr>
                    <td style="font-weight: bold; background: #f8fafc; border: 0.5px solid #cbd5e1; text-align: left; padding-left: 2mm;">Trocas de Contexto</td>
                    <td style="border: 0.5px solid #cbd5e1;">4</td>
                    <td style="border: 0.5px solid #cbd5e1; font-weight: bold; color: #dc2626;">7 (Máximo)</td>
                    <td style="border: 0.5px solid #cbd5e1;">4</td>
                    <td style="border: 0.5px solid #cbd5e1;">5</td>
                    <td style="border: 0.5px solid #cbd5e1;">4</td>
                    <td style="border: 0.5px solid #cbd5e1;">6</td>
                    <td style="border: 0.5px solid #cbd5e1;">6</td>
                </tr>
                <tr>
                    <td style="font-weight: bold; background: #f8fafc; border: 0.5px solid #cbd5e1; text-align: left; padding-left: 2mm;">Tempo Total de Execução</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                    <td style="border: 0.5px solid #cbd5e1;">14 s</td>
                </tr>
            </table>
        </div>
    </div>
</div>

</body>
</html>
"""

html_file = "temp_guia_visual.html"
pdf_file = "guia_visual_escalonamento_maziero.pdf"

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

cmd = [
    EDGE_PATH,
    '--headless',
    '--disable-gpu',
    f'--print-to-pdf={os.path.abspath(pdf_file)}',
    os.path.abspath(html_file)
]

subprocess.run(cmd, capture_output=True, check=True)

doc = fitz.open(pdf_file)
print(f"PDF gerado com sucesso: {pdf_file} com {doc.page_count} páginas")
doc.close()

if os.path.exists(html_file):
    os.remove(html_file)
