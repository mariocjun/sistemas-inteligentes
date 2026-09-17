import os
import re
import html
import subprocess
import fitz

EDGE_PATH = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

def get_p1_codes_html():
    with open('codigos_p1.md', 'r', encoding='utf-8') as f:
        text = f.read().replace('\r', '')

    # Extract all code blocks with their titles
    snippets = re.findall(r'### ([^\n]+)\n+```(\w*)\n(.*?)```', text, re.DOTALL)
    
    cards = []
    for title, lang, code in snippets:
        code_clean = code.strip('\n')
        # Extract chapter if available in title or context
        cap_badge = "Cap"
        if "Cap " in title:
            m = re.search(r'Cap (\d+)', title)
            if m: cap_badge = f"Cap {int(m.group(1)):02d}"
        elif "syscall" in title.lower():
            cap_badge = "Cap 02"
        elif any(k in title.lower() for k in ["processo", "thread", "tcb"]):
            cap_badge = "Cap 05"
        elif "posix" in title.lower() or "fila" in title.lower():
            cap_badge = "Cap 09"

        lang_tag = lang.upper() if lang else "C"
        
        cards.append(f"""
        <div class="code-card">
            <div class="code-header">
                <span class="badge-cap">{cap_badge}</span>
                <span class="code-title">{html.escape(title)}</span>
                <span class="badge-lang">{lang_tag}</span>
            </div>
            <pre class="code-content"><code>{html.escape(code_clean)}</code></pre>
        </div>
        """)
    return "\n".join(cards)

p1_codes_cards = get_p1_codes_html()

master_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Folhas de Consulta P1 - Sistemas Operacionais (Prof. Maziero)</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 5mm 6mm;
    }}
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #0f172a;
        background: #fff;
        font-size: 7pt;
        line-height: 1.25;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}
    .page {{
        page-break-after: always;
        height: 100%;
        display: flex;
        flex-direction: column;
        position: relative;
    }}
    .page:last-child {{
        page-break-after: auto;
    }}
    
    /* TOP HEADER */
    .top-header {{
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #fff;
        padding: 2mm 3.5mm;
        border-radius: 1.5mm;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2mm;
    }}
    .top-header .title {{
        font-size: 8.8pt;
        font-weight: 800;
        display: flex;
        align-items: center;
        gap: 2mm;
    }}
    .sheet-badge {{
        background: #2563eb;
        color: #fff;
        font-size: 6.8pt;
        font-weight: 700;
        padding: 0.5mm 2mm;
        border-radius: 0.8mm;
    }}
    .top-header .sub {{
        font-size: 6.2pt;
        color: #94a3b8;
    }}

    /* CODE CARDS (PAGE 1) */
    .code-grid {{
        column-count: 3;
        column-gap: 2.5mm;
        column-rule: 0.5px solid #cbd5e1;
        width: 100%;
        flex: 1;
    }}
    .code-card {{
        break-inside: avoid;
        margin-bottom: 1.5mm;
        border: 0.6px solid #cbd5e1;
        border-radius: 1mm;
        background: #fafafa;
        overflow: hidden;
    }}
    .code-header {{
        background: #f1f5f9;
        border-bottom: 0.6px solid #e2e8f0;
        padding: 0.6mm 1.5mm;
        font-size: 5.4pt;
        font-weight: 700;
        color: #334155;
        display: flex;
        align-items: center;
        gap: 1.2mm;
    }}
    .badge-cap {{
        background: #0284c7;
        color: #fff;
        padding: 0.2mm 0.8mm;
        border-radius: 0.5mm;
        font-weight: 800;
        font-size: 4.8pt;
    }}
    .code-title {{
        flex: 1;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    .badge-lang {{
        font-size: 4.4pt;
        color: #64748b;
        background: #e2e8f0;
        padding: 0.2mm 0.8mm;
        border-radius: 0.4mm;
        font-family: monospace;
    }}
    .code-content {{
        font-family: "Consolas", "Courier New", monospace;
        font-size: 4.6pt;
        letter-spacing: -0.15px;
        line-height: 1.08;
        padding: 0.8mm 1.2mm;
        white-space: pre;
        background: #ffffff;
        color: #0f172a;
        overflow: hidden;
    }}

    /* CONTENT CARDS */
    .card {{
        border: 0.6px solid #cbd5e1;
        border-radius: 1.4mm;
        background: #fff;
        margin-bottom: 2mm;
        overflow: hidden;
    }}
    .card-header {{
        background: #f8fafc;
        border-bottom: 0.6px solid #e2e8f0;
        padding: 1mm 2mm;
        font-weight: 700;
        font-size: 7.2pt;
        color: #1e293b;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .card-body {{
        padding: 1.5mm 2mm;
    }}

    /* GANTT CHARTS */
    .gantt-chart {{
        width: 100%;
        background: #fafafa;
        border: 0.5px solid #e2e8f0;
        border-radius: 1mm;
        padding: 1.5mm 2mm;
        margin: 1mm 0;
    }}
    .gantt-row {{
        display: flex;
        align-items: center;
        height: 4.4mm;
        margin-bottom: 0.8mm;
        position: relative;
    }}
    .task-lbl {{
        width: 6.5mm;
        font-weight: 800;
        font-size: 6.8pt;
        color: #334155;
    }}
    .gantt-track {{
        flex: 1;
        height: 100%;
        display: flex;
        position: relative;
        background: #fff;
        border-left: 1px solid #64748b;
        border-bottom: 1px solid #64748b;
    }}
    .box {{
        position: absolute;
        top: 0.4mm;
        bottom: 0.4mm;
        border-radius: 0.4mm;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 5.2pt;
        font-weight: 700;
        border: 0.5px solid #000;
    }}
    .box-wait {{ background: #ffffff; color: #475569; border: 0.5px solid #64748b; }}
    .box-t1 {{ background: #2563eb; color: #fff; }}
    .box-t2 {{ background: #eab308; color: #000; }}
    .box-t3 {{ background: #9333ea; color: #fff; }}
    .box-t4 {{ background: #16a34a; color: #fff; }}
    .box-t5 {{ background: #dc2626; color: #fff; }}

    .gantt-axis {{
        display: flex;
        margin-left: 6.5mm;
        height: 3.5mm;
        border-top: 1px solid #64748b;
    }}
    .axis-tick {{
        flex: 1;
        font-size: 5.5pt;
        color: #64748b;
        text-align: left;
        padding-top: 0.4mm;
        position: relative;
    }}
    .axis-tick::before {{
        content: "";
        position: absolute;
        top: -1px;
        left: 0;
        width: 1px;
        height: 1.2mm;
        background: #64748b;
    }}
    .axis-tick-end {{
        width: 0;
        font-size: 5.5pt;
        color: #64748b;
        position: relative;
        padding-top: 0.4mm;
    }}
    .axis-tick-end::before {{
        content: "";
        position: absolute;
        top: -1px;
        left: 0;
        width: 1px;
        height: 1.2mm;
        background: #64748b;
    }}

    /* TABLES & CALLOUTS */
    .metrics-pill {{
        background: #f1f5f9;
        border: 0.5px solid #cbd5e1;
        padding: 0.4mm 1.5mm;
        border-radius: 0.6mm;
        font-weight: 700;
        font-size: 6.2pt;
    }}
    .didactic-box {{
        background: #eff6ff;
        border-left: 2px solid #3b82f6;
        padding: 1.2mm 2mm;
        border-radius: 0 1mm 1mm 0;
        font-size: 6.2pt;
        margin-top: 1mm;
    }}
    .didactic-box ol, .didactic-box ul {{
        margin-left: 3mm;
        margin-top: 0.5mm;
    }}
    .didactic-box li {{
        margin-bottom: 0.4mm;
    }}

    .rr-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 5.8pt;
        margin-top: 1mm;
    }}
    .rr-table th, .rr-table td {{
        border: 0.5px solid #cbd5e1;
        padding: 0.6mm 1mm;
        text-align: center;
    }}
    .rr-table th {{
        background: #1e293b;
        color: #fff;
    }}
    .rr-table tr:nth-child(even) {{
        background: #f8fafc;
    }}
</style>
</head>
<body>

<!-- =========================================================================
     PÁGINA 1 (FOLHA 1 - FRENTE): CÓDIGOS OFICIAIS DE PROGRAMAÇÃO (AT01)
     ========================================================================= -->
<div class="page">
    <div class="top-header">
        <div class="title">
            <span class="sheet-badge">FOLHA 1 — FRENTE</span>
            <span>Códigos de Sistemas Operacionais (P1 / AT01: Capítulos 01 a 09)</span>
        </div>
        <div class="sub">Syscalls C/ASM, TCB Linux, Processos, Pthreads, POSIX Queues</div>
    </div>
    
    <div class="code-grid">
        {p1_codes_cards}
    </div>
</div>

<!-- =========================================================================
     PÁGINA 2 (FOLHA 1 - VERSO): REGRAS DO DESENHO, FÓRMULAS, FCFS E SJF
     ========================================================================= -->
<div class="page">
    <div class="top-header">
        <div class="title">
            <span class="sheet-badge">FOLHA 1 — VERSO</span>
            <span>Teoria do Escalonador, Fórmulas Algébricas e Algoritmos Cooperativos</span>
        </div>
        <div class="sub">Como Desenhar sem Errar • FCFS e SJF Passo a Passo</div>
    </div>

    <!-- REGRAS E DADOS CANONICOS -->
    <div class="card" style="margin-bottom: 1.5mm;">
        <div class="card-header">
            <span>📐 O Modelo Mental do Maziero e as Fórmulas Invariantes</span>
            <span style="font-size: 6.2pt; color: #475569;">Não conte quadradinhos vazios para achar espera!</span>
        </div>
        <div class="card-body" style="padding: 1.2mm 2mm; display: flex; gap: 2mm;">
            <div style="flex: 1.2; font-size: 6.2pt;">
                <strong>Fórmulas Matemáticas:</strong>
                <br>• <strong>Tempo de Retorno / Vida (Turnaround):</strong> <span style="background:#e0f2fe; padding:0.2mm 1mm; font-weight:bold;">t_t(i) = f_i - c_i</span> (fim menos chegada).
                <br>• <strong>Tempo de Espera (Waiting):</strong> <span style="background:#fef3c7; padding:0.2mm 1mm; font-weight:bold;">t_w(i) = t_t(i) - d_i = f_i - c_i - d_i</span> (fim - chegada - duração).
                <br>• <strong>Tempo de Resposta (Response):</strong> <span style="background:#dcfce7; padding:0.2mm 1mm; font-weight:bold;">t_r(i) = p_i - c_i</span> (primeira execução menos chegada).
                <br>• <strong>Médias Gerais:</strong> T_t = &sum; t_t / N  |  T_w = &sum; t_w / N.
            </div>
            <div style="flex: 1; font-size: 6pt; border-left: 1px solid #cbd5e1; padding-left: 2mm;">
                <strong>O Exemplo Canônico do Capítulo 06:</strong>
                <br>• <strong>t1:</strong> Ingresso 0 | Dur 5 | Prio 2 (🟦 Azul)
                <br>• <strong>t2:</strong> Ingresso 0 | Dur 2 | Prio 3 (🟨 Amarelo)
                <br>• <strong>t3:</strong> Ingresso 1 | Dur 4 | Prio 1 (🟪 Roxo)
                <br>• <strong>t4:</strong> Ingresso 3 | Dur 1 | Prio 4 (🟩 Verde)
                <br>• <strong>t5:</strong> Ingresso 5 | Dur 2 | Prio 5 (🟥 Vermelho)
            </div>
        </div>
    </div>

    <!-- 1. FCFS -->
    <div class="card" style="margin-bottom: 1.5mm;">
        <div class="card-header">
            <span>1. Escalonamento FCFS (First Come, First Served)</span>
            <span class="metrics-pill">Tt = 8,0 s | Tw = 5,2 s | 4 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*7/14);">Espera [5 a 12] (7s)</div><div class="box box-t5" style="left:calc(100%*12/14); width:calc(100%*2/14);">CPU [12-14]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*8/14);">Espera [3 a 11] (8s)</div><div class="box box-t4" style="left:calc(100%*11/14); width:calc(100%*1/14);">CPU</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*6/14);">Espera [1 a 7] (6s)</div><div class="box box-t3" style="left:calc(100%*7/14); width:calc(100%*4/14);">CPU [7 a 11] (4s)</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*5/14);">Espera [0 a 5] (5s)</div><div class="box box-t2" style="left:calc(100%*5/14); width:calc(100%*2/14);">CPU (2s)</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-t1" style="left:0; width:calc(100%*5/14);">CPU [0 a 5] (5s)</div></div></div>
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-box">
                <strong>Passo a Passo de Desenho e Contas (FCFS):</strong>
                <br>1. Ordene estritamente por chegada: t1(0) &rarr; t2(0) &rarr; t3(1) &rarr; t4(3) &rarr; t5(5).
                <br>2. t1 roda [0 a 5] &rArr; f1 = 5, tt = 5-0 = 5s, tw = 5-5 = 0s.
                <br>3. t2 espera de 0 a 5 e roda [5 a 7] &rArr; f2 = 7, tt = 7-0 = 7s, tw = 7-2 = 5s.
                <br>4. t3 espera de 1 a 7 e roda [7 a 11] &rArr; f3 = 11, tt = 11-1 = 10s, tw = 10-4 = 6s.
                <br>5. t4 espera de 3 a 11 e roda [11 a 12] &rArr; f4 = 12, tt = 9s, tw = 8s.  |  t5 espera [5 a 12] e roda [12 a 14] &rArr; f5 = 14, tt = 9s, tw = 7s.
            </div>
        </div>
    </div>

    <!-- 2. SJF -->
    <div class="card">
        <div class="card-header">
            <span>2. Escalonamento SJF (Shortest Job First - Cooperativo)</span>
            <span class="metrics-pill">Tt = 5,8 s | Tw = 3,0 s | 4 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">Espera (2s)</div><div class="box box-t5" style="left:calc(100%*7/14); width:calc(100%*2/14);">CPU [7 a 9]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*3/14);">Espera (3s)</div><div class="box box-t4" style="left:calc(100%*6/14); width:calc(100%*1/14);">CPU</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*1/14);">Esp</div><div class="box box-t3" style="left:calc(100%*2/14); width:calc(100%*4/14);">CPU [2 a 6] (4s)</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*2/14);">CPU [0 a 2]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*9/14);">Espera [0 a 9] (9s)</div><div class="box box-t1" style="left:calc(100%*9/14); width:calc(100%*5/14);">CPU [9 a 14] (5s)</div></div></div>
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-box">
                <strong>Passo a Passo de Desenho e Decisões em Cada Término (SJF):</strong>
                <br>• <strong>t = 0:</strong> Prontas {{t1(d=5), t2(d=2)}}. Menor d é t2 &rArr; pinte t2 [0 a 2].
                <br>• <strong>t = 2:</strong> t2 acabou. Prontas {{t1(5), t3(4)}}. Menor d é t3 &rArr; pinte t3 [2 a 6].
                <br>• <strong>t = 6:</strong> t3 acabou. Prontas {{t1(5), t4(1), t5(2)}}. Menor d é t4 &rArr; pinte t4 [6 a 7].
                <br>• <strong>t = 7:</strong> t4 acabou. Prontas {{t1(5), t5(2)}}. Menor d é t5 &rArr; pinte t5 [7 a 9].
                <br>• <strong>t = 9:</strong> Só resta t1 &rArr; pinte t1 [9 a 14]. Conclusões: f = [14, 2, 6, 7, 9] &rArr; Tw = [9, 0, 1, 3, 2] &rArr; Média Tw = 3,0 s.
            </div>
        </div>
    </div>
</div>

<!-- =========================================================================
     PÁGINA 3 (FOLHA 2 - FRENTE): PREEMPTIVOS: SRTF E ROUND-ROBIN
     ========================================================================= -->
<div class="page">
    <div class="top-header">
        <div class="title">
            <span class="sheet-badge">FOLHA 2 — FRENTE</span>
            <span>Escalonadores Preemptivos: SRTF e Round-Robin (Capítulo 06)</span>
        </div>
        <div class="sub">Preempção por Menor Restante • O Diagrama da Fila do Slide 11 Passo a Passo</div>
    </div>

    <!-- 3. SRTF -->
    <div class="card" style="margin-bottom: 1.5mm;">
        <div class="card-header">
            <span>3. Escalonamento SRTF (Shortest Remaining Time First)</span>
            <span class="metrics-pill">Tt = 5,4 s (Mínimo) | Tw = 2,6 s | 5 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">Espera</div><div class="box box-t5" style="left:calc(100%*7/14); width:calc(100%*2/14);">CPU [7 a 9]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-t4" style="left:calc(100%*3/14); width:calc(100%*1/14);">CPU [3-4]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*1/14);">Esp</div><div class="box box-t3" style="left:calc(100%*2/14); width:calc(100%*1/14);">CPU</div><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*1/14);">Preemptada</div><div class="box box-t3" style="left:calc(100%*4/14); width:calc(100%*3/14);">CPU [4 a 7] (3s)</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*2/14);">CPU [0 a 2]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*9/14);">Espera [0 a 9] (9s)</div><div class="box box-t1" style="left:calc(100%*9/14); width:calc(100%*5/14);">CPU [9 a 14] (5s)</div></div></div>
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>
            <div class="didactic-box">
                <strong>O Ponto Crítico de Desenho (Preempção em t = 3):</strong>
                <br>• Em t = 2, t3 começa a rodar. Em t = 3, chega t4(d=1). Resta de t3 = 3 s. Como 1 &lt; 3, <strong>t4 preempta t3</strong>!
                <br>• <em>No desenho:</em> <strong>corte a barra colorida de t3 em 3</strong>, pinte t4 em [3-4], deixe caixa branca de espera em t3 em [3-4], e retome t3 em 4!
            </div>
        </div>
    </div>

    <!-- 4. ROUND-ROBIN -->
    <div class="card">
        <div class="card-header">
            <span>4. Escalonamento Round-Robin (Revezamento com Quantum tq = 2) — O Slide 11 Passo a Passo</span>
            <span class="metrics-pill">Tt = 8,4 s | Tw = 5,6 s | 7 Trocas (Máximo)</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*4/14);">Espera</div><div class="box box-t5" style="left:calc(100%*9/14); width:calc(100%*2/14);">CPU [9-11]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*5/14);">Espera (5s)</div><div class="box box-t4" style="left:calc(100%*8/14); width:calc(100%*1/14);">CPU</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*3/14);">Espera</div><div class="box box-t3" style="left:calc(100%*4/14); width:calc(100%*2/14);">CPU [4-6]</div><div class="box box-wait" style="left:calc(100%*6/14); width:calc(100%*5/14);">Espera (5s)</div><div class="box box-t3" style="left:calc(100%*11/14); width:calc(100%*2/14);">CPU [11-13]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*2/14);">Esp</div><div class="box box-t2" style="left:calc(100%*2/14); width:calc(100%*2/14);">CPU [2 a 4]</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-t1" style="left:0; width:calc(100%*2/14);">CPU [0-2]</div><div class="box box-wait" style="left:calc(100%*2/14); width:calc(100%*4/14);">Espera</div><div class="box box-t1" style="left:calc(100%*6/14); width:calc(100%*2/14);">CPU [6-8]</div><div class="box box-wait" style="left:calc(100%*8/14); width:calc(100%*5/14);">Espera</div><div class="box box-t1" style="left:calc(100%*13/14); width:calc(100%*1/14);">CPU</div></div></div>
                <div class="gantt-axis">
                    <div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div>
                    <div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div>
                    <div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div>
                </div>
            </div>

            <!-- TABELA DO SLIDE 11 -->
            <table class="rr-table">
                <thead>
                    <tr>
                        <th style="width: 8mm;">Tempo</th><th>Fila Prontos</th><th>CPU</th><th>Evento / Transição Didática</th>
                        <th style="width: 8mm;">Tempo</th><th>Fila Prontos</th><th>CPU</th><th>Evento / Transição Didática</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>t = 0</td><td>[ t2 ]</td><td><span class="box-t1" style="padding:0.2mm 0.8mm;">t1</span></td><td>t1 entra na CPU; t2 aguarda na fila</td><td>t = 8</td><td>[ t1, t3, t5 ]</td><td><span class="box-t4" style="padding:0.2mm 0.8mm;">t4</span></td><td>t4 roda 1 s e conclui</td></tr>
                    <tr><td>t = 1</td><td>[ t3, t2 ]</td><td><span class="box-t1" style="padding:0.2mm 0.8mm;">t1</span></td><td>t3 chega e entra no fim da fila</td><td>t = 9</td><td>[ t1, t3 ]</td><td><span class="box-t5" style="padding:0.2mm 0.8mm;">t5</span></td><td>t4 conclui (FIM); t5 assume a CPU</td></tr>
                    <tr><td>t = 2</td><td>[ t1, t3 ]</td><td><span class="box-t2" style="padding:0.2mm 0.8mm;">t2</span></td><td>Fim do quantum de t1; t2 assume a CPU</td><td>t = 10</td><td>[ t1, t3 ]</td><td><span class="box-t5" style="padding:0.2mm 0.8mm;">t5</span></td><td>t5 completa seu 2º segundo de fatia</td></tr>
                    <tr><td>t = 3</td><td>[ t4, t1, t3 ]</td><td><span class="box-t2" style="padding:0.2mm 0.8mm;">t2</span></td><td>t4 chega e entra no fim da fila</td><td>t = 11</td><td>[ t1 ]</td><td><span class="box-t3" style="padding:0.2mm 0.8mm;">t3</span></td><td>t5 conclui (FIM); t3 assume a CPU</td></tr>
                    <tr><td>t = 4</td><td>[ t4, t1 ]</td><td><span class="box-t3" style="padding:0.2mm 0.8mm;">t3</span></td><td>t2 conclui (FIM); t3 assume a CPU</td><td>t = 12</td><td>[ t1 ]</td><td><span class="box-t3" style="padding:0.2mm 0.8mm;">t3</span></td><td>t3 completa seu 2º segundo de fatia</td></tr>
                    <tr><td>t = 5</td><td>[ t5, t4, t1 ]</td><td><span class="box-t3" style="padding:0.2mm 0.8mm;">t3</span></td><td>t5 chega e entra no fim da fila</td><td>t = 13</td><td>[ vazio ]</td><td><span class="box-t1" style="padding:0.2mm 0.8mm;">t1</span></td><td>t3 conclui (FIM); t1 roda seu 1 s final</td></tr>
                    <tr><td>t = 6</td><td>[ t3, t5, t4 ]</td><td><span class="box-t1" style="padding:0.2mm 0.8mm;">t1</span></td><td>Fim do quantum de t3; t1 assume a CPU</td><td>t = 14</td><td>[ vazio ]</td><td>—</td><td>t1 conclui (FIM). Todas finalizadas!</td></tr>
                    <tr><td>t = 7</td><td>[ t3, t5, t4 ]</td><td><span class="box-t1" style="padding:0.2mm 0.8mm;">t1</span></td><td>t1 completa seu 2º segundo na CPU</td><td colspan="4" style="background:#f1f5f9; font-weight:bold; color:#1e40af;">Regra: Novas chegadas entram ANTES de quem sofre preempção!</td></tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- =========================================================================
     PÁGINA 4 (FOLHA 2 - VERSO): PRIORIDADES, AGING, COMPARATIVO E INVERSÃO
     ========================================================================= -->
<div class="page">
    <div class="top-header">
        <div class="title">
            <span class="sheet-badge">FOLHA 2 — VERSO</span>
            <span>Prioridades, Aging, Quadro Comparativo & Inversão de Prioridade</span>
        </div>
        <div class="sub">PRIOc, PRIOp, PRIOd (Slide 23) • Gabarito Teórico Oficial • Questão de Prova</div>
    </div>

    <!-- PRIOc e PRIOp LADO A LADO -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2mm; margin-bottom: 1.2mm;">
        <!-- PRIOc -->
        <div class="card">
            <div class="card-header">
                <span>5. PRIOc (Prioridade Cooperativa)</span>
                <span class="metrics-pill">Tt=6,6s | Tw=3,8s</span>
            </div>
            <div class="card-body">
                <div class="gantt-chart">
                    <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">Esp</div><div class="box box-t5" style="left:calc(100%*7/14); width:calc(100%*2/14);">CPU [7-9]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*6/14);">Espera</div><div class="box box-t4" style="left:calc(100%*9/14); width:calc(100%*1/14);">CPU</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*9/14);">Espera [1 a 10]</div><div class="box box-t3" style="left:calc(100%*10/14); width:calc(100%*4/14);">CPU</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*2/14);">CPU [0-2]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*2/14);">Esp</div><div class="box box-t1" style="left:calc(100%*2/14); width:calc(100%*5/14);">CPU [2 a 7]</div></div></div>
                    <div class="gantt-axis"><div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div><div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div><div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div></div>
                </div>
                <div style="font-size: 5.4pt; color: #475569; margin-top: 0.6mm;">
                    Ordem: t2(p=3) &rarr; t1(p=2) &rarr; t5(p=5) &rarr; t4(p=4) &rarr; t3(p=1). Como é cooperativo, ninguém interrompe t1 em 3 ou 5.
                </div>
            </div>
        </div>

        <!-- PRIOp -->
        <div class="card">
            <div class="card-header">
                <span>6. PRIOp (Prioridade Preemptiva)</span>
                <span class="metrics-pill">Tt=5,6s | Tw=2,8s</span>
            </div>
            <div class="card-body">
                <div class="gantt-chart">
                    <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-t5" style="left:calc(100%*5/14); width:calc(100%*2/14);">CPU [5-7]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-t4" style="left:calc(100%*3/14); width:calc(100%*1/14);">CPU [3-4]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*9/14);">Espera [1 a 10]</div><div class="box box-t3" style="left:calc(100%*10/14); width:calc(100%*4/14);">CPU [10-14]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*2/14);">CPU [0-2]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*2/14);">Esp</div><div class="box box-t1" style="left:calc(100%*2/14); width:calc(100%*1/14);">1s</div><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*1/14);">P</div><div class="box box-t1" style="left:calc(100%*4/14); width:calc(100%*1/14);">1s</div><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">P</div><div class="box box-t1" style="left:calc(100%*7/14); width:calc(100%*3/14);">3s [7-10]</div></div></div>
                    <div class="gantt-axis"><div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div><div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div><div class="axis-tick-end">14</div></div>
                </div>
                <div style="font-size: 5.4pt; color: #475569; margin-top: 0.6mm;">
                    <strong>Duas preempções em t1:</strong> Cortada em t=3 por t4(p=4) e em t=5 por t5(p=5). Barra de t1 fatiada em: [2-3], [4-5] e [7-10].
                </div>
            </div>
        </div>
    </div>

    <!-- 7. PRIOd (AGING) -->
    <div class="card" style="margin-bottom: 1.2mm;">
        <div class="card-header">
            <span>7. Escalonamento PRIOd (Prioridade Dinâmica / Aging com &alpha; = 1) — Fiel ao Slide 23</span>
            <span class="metrics-pill">Tt = 5,8 s | Tw = 3,0 s | 6 Trocas</span>
        </div>
        <div class="card-body">
            <div class="gantt-chart">
                <div class="gantt-row"><div class="task-lbl">t5</div><div class="gantt-track"><div class="box box-t5" style="left:calc(100%*5/14); width:calc(100%*2/14);">5 (CPU [5-7])</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t4</div><div class="gantt-track"><div class="box box-t4" style="left:calc(100%*3/14); width:calc(100%*1/14);">4 (CPU [3-4])</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t3</div><div class="gantt-track"><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*1/14);">2</div><div class="box box-wait" style="left:calc(100%*2/14); width:calc(100%*1/14);">3</div><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*1/14);">4</div><div class="box box-t3" style="left:calc(100%*4/14); width:calc(100%*1/14);">1</div><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*1/14);">2</div><div class="box box-wait" style="left:calc(100%*6/14); width:calc(100%*1/14);">3</div><div class="box box-wait" style="left:calc(100%*7/14); width:calc(100%*1/14);">4</div><div class="box box-wait" style="left:calc(100%*8/14); width:calc(100%*1/14);">5</div><div class="box box-wait" style="left:calc(100%*9/14); width:calc(100%*1/14);">6</div><div class="box box-wait" style="left:calc(100%*10/14); width:calc(100%*1/14);">7</div><div class="box box-t3" style="left:calc(100%*11/14); width:calc(100%*3/14);">1 (CPU [11 a 14])</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t2</div><div class="gantt-track"><div class="box box-t2" style="left:0; width:calc(100%*1/14);">3</div><div class="box box-t2" style="left:calc(100%*1/14); width:calc(100%*1/14);">3</div></div></div>
                <div class="gantt-row"><div class="task-lbl">t1</div><div class="gantt-track"><div class="box box-wait" style="left:0; width:calc(100%*1/14);">3</div><div class="box box-wait" style="left:calc(100%*1/14); width:calc(100%*1/14);">4</div><div class="box box-t1" style="left:calc(100%*2/14); width:calc(100%*1/14);">2</div><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*1/14);">3</div><div class="box box-wait" style="left:calc(100%*4/14); width:calc(100%*1/14);">4</div><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*2/14);">5</div><div class="box box-t1" style="left:calc(100%*7/14); width:calc(100%*4/14);">2 (CPU [7 a 11])</div></div></div>
                <div class="gantt-axis"><div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div><div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick-end">14</div></div>
            </div>
            <div class="didactic-box" style="margin-top: 0.8mm; padding: 1mm 1.5mm;">
                <strong>O Segredo dos Números no Desenho (Slide 23):</strong> Anote a prioridade dinâmica (pd) em cada segundo!
                <br>• Se espera na fila: <strong>pd &larr; pd + 1</strong>. Se executa na CPU: reseta para a prioridade estática original <strong>pd &larr; pe</strong>.
                <br>• Em t = 4, t3 esperou 3s e sua prioridade subiu para 4 (igual a t1); desempata e ganha a CPU, evitando inanição (starvation)!
            </div>
        </div>
    </div>

    <!-- COMPARATIVO E CASO DE PROVA LADO A LADO -->
    <div style="display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 2mm;">
        <!-- TABELA COMPARATIVA -->
        <div class="card">
            <div class="card-header"><span>📊 Quadro Comparativo Oficial (Slide 26)</span></div>
            <div class="card-body" style="padding: 0.8mm 1.2mm;">
                <table style="width: 100%; border-collapse: collapse; font-size: 5.6pt; text-align: center;">
                    <tr style="background:#1e293b; color:#fff; font-weight:bold;">
                        <td style="padding:0.5mm; border:0.5px solid #475569;">Algoritmo</td>
                        <td style="border:0.5px solid #475569;">Tt médio</td>
                        <td style="border:0.5px solid #475569;">Tw médio</td>
                        <td style="border:0.5px solid #475569;">Trocas</td>
                    </tr>
                    <tr><td style="font-weight:bold; border:0.5px solid #cbd5e1;">FCFS</td><td style="border:0.5px solid #cbd5e1;">8,0 s</td><td style="border:0.5px solid #cbd5e1;">5,2 s</td><td style="border:0.5px solid #cbd5e1;">4</td></tr>
                    <tr><td style="font-weight:bold; border:0.5px solid #cbd5e1; color:#dc2626;">RR (q=2)</td><td style="border:0.5px solid #cbd5e1;">8,4 s</td><td style="border:0.5px solid #cbd5e1;">5,6 s</td><td style="border:0.5px solid #cbd5e1; font-weight:bold;">7 (Máx)</td></tr>
                    <tr><td style="font-weight:bold; border:0.5px solid #cbd5e1;">SJF</td><td style="border:0.5px solid #cbd5e1;">5,8 s</td><td style="border:0.5px solid #cbd5e1;">3,0 s</td><td style="border:0.5px solid #cbd5e1;">4</td></tr>
                    <tr style="background:#dbeafe; font-weight:bold;"><td style="border:0.5px solid #93c5fd;">SRTF</td><td style="border:0.5px solid #93c5fd;">5,4 s (Mín)</td><td style="border:0.5px solid #93c5fd;">2,6 s (Mín)</td><td style="border:0.5px solid #93c5fd;">5</td></tr>
                    <tr><td style="font-weight:bold; border:0.5px solid #cbd5e1;">PRIOc</td><td style="border:0.5px solid #cbd5e1;">6,6 s</td><td style="border:0.5px solid #cbd5e1;">3,8 s</td><td style="border:0.5px solid #cbd5e1;">4</td></tr>
                    <tr><td style="font-weight:bold; border:0.5px solid #cbd5e1;">PRIOp</td><td style="border:0.5px solid #cbd5e1;">5,6 s</td><td style="border:0.5px solid #cbd5e1;">2,8 s</td><td style="border:0.5px solid #cbd5e1;">6</td></tr>
                    <tr><td style="font-weight:bold; border:0.5px solid #cbd5e1;">PRIOd</td><td style="border:0.5px solid #cbd5e1;">5,8 s</td><td style="border:0.5px solid #cbd5e1;">3,0 s</td><td style="border:0.5px solid #cbd5e1;">6</td></tr>
                </table>
            </div>
        </div>

        <!-- CASO DE PROVA: INVERSÃO DE PRIORIDADE COM GRÁFICO E RESPOSTAS -->
        <div class="card">
            <div class="card-header">
                <span>🚨 Questão de Prova: Inversão de Prioridade & PMC</span>
                <span style="font-size:5pt; background:#fef2f2; color:#b91c1c; padding:0.2mm 1mm; border-radius:0.4mm; font-weight:bold;">25 Pontos Moodle</span>
            </div>
            <div class="card-body" style="padding: 0.8mm 1.5mm;">
                <!-- GANTT DA QUESTÃO -->
                <div class="gantt-chart" style="margin-bottom: 1mm;">
                    <div class="gantt-row"><div class="task-lbl" style="font-size:5.2pt;">t3(p=5)</div><div class="gantt-track"><div class="box box-t3" style="left:calc(100%*5/14); width:calc(100%*1/14); font-size:4.4pt;">CPU</div><div class="box" style="left:calc(100%*6/14); width:calc(100%*5/14); background:#fee2e2; color:#991b1b; border:0.5px dashed #dc2626; font-size:4.4pt; font-weight:bold;">⛔ Bloq PMC</div><div class="box box-t3" style="left:calc(100%*11/14); width:calc(100%*2/14); font-size:4.4pt; font-weight:bold;">PMC [11-13]</div></div></div>
                    <div class="gantt-row"><div class="task-lbl" style="font-size:5.2pt;">t2(p=3)</div><div class="gantt-track"><div class="box box-t2" style="left:calc(100%*3/14); width:calc(100%*2/14); font-size:4.4pt;">CPU [3-5]</div><div class="box box-wait" style="left:calc(100%*5/14); width:calc(100%*1/14); font-size:4.4pt;">P</div><div class="box box-t2" style="left:calc(100%*6/14); width:calc(100%*4/14); font-size:4.5pt; font-weight:bold; background:#fbbf24;">⚡ INVERSÃO [6-10] (FIM)</div></div></div>
                    <div class="gantt-row"><div class="task-lbl" style="font-size:5.2pt;">t1(p=2)</div><div class="gantt-track"><div class="box box-t1" style="left:0; width:calc(100%*2/14); font-size:4.4pt;">CPU [0-2]</div><div class="box box-t1" style="left:calc(100%*2/14); width:calc(100%*1/14); background:#1d4ed8; font-size:4.4pt; font-weight:bold;">PMC</div><div class="box box-wait" style="left:calc(100%*3/14); width:calc(100%*7/14); font-size:4.4pt;">Preemptada (segura PMC)</div><div class="box box-t1" style="left:calc(100%*10/14); width:calc(100%*1/14); background:#1d4ed8; font-size:4.4pt; font-weight:bold;">PMC</div><div class="box box-wait" style="left:calc(100%*11/14); width:calc(100%*2/14); font-size:4.4pt;">P</div><div class="box box-t1" style="left:calc(100%*13/14); width:calc(100%*1/14); font-size:4.4pt;">FIM</div></div></div>
                    <div class="gantt-axis" style="height:2.8mm;"><div class="axis-tick">0</div><div class="axis-tick">1</div><div class="axis-tick">2</div><div class="axis-tick">3</div><div class="axis-tick">4</div><div class="axis-tick">5</div><div class="axis-tick">6</div><div class="axis-tick">7</div><div class="axis-tick">8</div><div class="axis-tick">9</div><div class="axis-tick">10</div><div class="axis-tick">11</div><div class="axis-tick">12</div><div class="axis-tick">13</div><div class="axis-tick-end">14</div></div>
                </div>

                <!-- TABELA DE GABARITO DAS 7 PERGUNTAS -->
                <table style="width: 100%; border-collapse: collapse; font-size: 5.2pt;">
                    <tr style="background:#f1f5f9; font-weight:bold;">
                        <td style="border:0.5px solid #cbd5e1; padding:0.4mm;">Campo da Questão na Prova</td>
                        <td style="border:0.5px solid #cbd5e1; text-align:center; width:12mm;">Instante</td>
                        <td style="border:0.5px solid #cbd5e1; padding:0.4mm;">Motivo / Dedução Direta</td>
                    </tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t1 solicita acesso exclusivo a PMC:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#dcfce7;">2</td><td style="border:0.5px solid #cbd5e1;">Dado explícito no enunciado da questão.</td></tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t1 recebe acesso exclusivo a PMC:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#dcfce7;">2</td><td style="border:0.5px solid #cbd5e1;">PMC estava livre; ganha de imediato.</td></tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t1 libera a PMC:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#fee2e2;">11</td><td style="border:0.5px solid #cbd5e1;">Executa 1s em [2-3], é preemptada por t2, retoma em 10 e roda +1s em [10-11].</td></tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t3 solicita acesso exclusivo a PMC:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#dcfce7;">6</td><td style="border:0.5px solid #cbd5e1;">Inicia em t=5; solicita 1 unidade após o início (5 + 1 = 6).</td></tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t3 recebe acesso exclusivo a PMC:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#fee2e2;">11</td><td style="border:0.5px solid #cbd5e1;">Fica bloqueada de 6 a 11; acorda no momento que t1 libera em 11.</td></tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t3 libera a PMC:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#fee2e2;">13</td><td style="border:0.5px solid #cbd5e1;">Roda sua seção crítica de 2 unidades inteiramente em [11-13] (11 + 2 = 13).</td></tr>
                    <tr><td style="border:0.5px solid #cbd5e1;">t2 termina sua execução:</td><td style="border:0.5px solid #cbd5e1; text-align:center; font-weight:bold; background:#fef3c7;">10</td><td style="border:0.5px solid #cbd5e1;">Roda 2s em [3-5], retoma em 6 (inversão enquanto t3 bloqueia) e conclui em 10.</td></tr>
                </table>
            </div>
        </div>
    </div>
</div>
</div>

</body>
</html>
"""

output_pdf = "folhas_consulta_P1_2folhas_4paginas.pdf"
temp_html = "temp_master_4p.html"

with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(master_html)

cmd = [
    EDGE_PATH,
    '--headless',
    '--disable-gpu',
    f'--print-to-pdf={os.path.abspath(output_pdf)}',
    os.path.abspath(temp_html)
]

subprocess.run(cmd, capture_output=True, check=True)

doc = fitz.open(output_pdf)
print(f"Master PDF gerado: {output_pdf} com {doc.page_count} páginas")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    img_name = f"folha_consulta_p{i+1}.png"
    pix.save(img_name)
    print(f"Renderizada página {i+1}: {img_name}")
doc.close()

if os.path.exists(temp_html):
    os.remove(temp_html)
