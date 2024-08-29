"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class Diferenciador(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Diferenciador',  # Nombre que aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior = 0

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal de salida (derivada)
        N = len(x)
        
        # Calcular la derivada
        y0[0] = x[0] - self.acum_anterior
        for i in range(1, N):
            y0[i] = x[i] - x[i - 1]

        # Actualizar el valor acumulado
        self.acum_anterior = x[N - 1]

        return len(y0)

