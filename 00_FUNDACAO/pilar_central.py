#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
pilar_central.py - Os 3 Pilares Fundamentais
"""

import sys

class PilarCentral:
    def __init__(self):
        self.nome = "pilar_central"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = PilarCentral()
    print(obj.ativar())
