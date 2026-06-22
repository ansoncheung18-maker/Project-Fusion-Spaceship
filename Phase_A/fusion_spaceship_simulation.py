# ============================================================
# 核聚變飛船專案 Phase A：性能模擬
# 目標：計算飛船嘅 Delta-V、飛行時間、燃料需求
# ============================================================

import math

print("="*60)
print("核聚變飛船性能模擬")
print("="*60)

# ============================================================
# 1. 基本參數
# ============================================================

# 飛船參數
dry_mass_kg = 500_000  # 乾質量 500 噸（結構、反應爐、貨物）
fuel_mass_kg = 100_000  # 燃料質量 100 噸（氘）
initial_mass_kg = dry_mass_kg + fuel_mass_kg

# 推進參數
isp = 8000  # 比衝 8,000 秒（保守估算）
g0 = 9.81  # 地球重力加速度
exhaust_velocity = isp * g0  # 排氣速度 (m/s)

print("\n【飛船參數】")
print(f"乾質量: {dry_mass_kg/1000:.0f} 噸")
print(f"燃料質量: {fuel_mass_kg/1000:.0f} 噸")
print(f"總質量: {initial_mass_kg/1000:.0f} 噸")
print(f"比衝 (Isp): {isp} 秒")
print(f"排氣速度: {exhaust_velocity:.0f} m/s")

# ============================================================
# 2. Delta-V 計算 (Tsiolkovsky 火箭方程)
# ============================================================

delta_v = exhaust_velocity * math.log(initial_mass_kg / dry_mass_kg)
delta_v_kms = delta_v / 1000

print("\n【Delta-V 計算】")
print(f"Delta-V: {delta_v_kms:.2f} km/s")

# ============================================================
# 3. 飛行時間計算
# ============================================================

# 假設一半 Delta-V 用於加速，一半用於減速
accel_delta_v = delta_v / 2

# 加速階段距離 (假設勻加速)
# d = v^2 / (2 * a)，但用 Delta-V 估算
# 對於霍曼轉移，可以用 Delta-V 估算飛行時間

# 火星轉移（簡化計算）
mars_transfer_dv = 4.5  # km/s（火星轉移所需 Delta-V）
mars_travel_time_days = (mars_transfer_dv / delta_v_kms) * 180  # 粗略估算

print("\n【飛行時間估算】")
print(f"可用 Delta-V: {delta_v_kms:.2f} km/s")
print(f"火星轉移所需 Delta-V: 約 4.5 km/s")
print(f"預估火星飛行時間: {mars_travel_time_days:.0f} 天")

# ============================================================
# 4. 對比化學火箭
# ============================================================

# 化學火箭參數 (Starship 參考)
chemical_isp = 350
chemical_exhaust = chemical_isp * g0
chemical_dv = chemical_exhaust * math.log(initial_mass_kg / dry_mass_kg)
chemical_dv_kms = chemical_dv / 1000

print("\n【對比化學火箭】")
print(f"化學火箭比衝: {chemical_isp} 秒")
print(f"化學火箭 Delta-V: {chemical_dv_kms:.2f} km/s")
print(f"核聚變飛船 Delta-V: {delta_v_kms:.2f} km/s")
print(f"核聚變飛船係化學火箭嘅 {delta_v_kms / chemical_dv_kms:.1f} 倍")

# ============================================================
# 5. 燃料成本
# ============================================================

# 氘燃料成本（海水提取）
deuterium_price_per_kg = 100  # 假設 $100/kg（保守估算）
fuel_cost = fuel_mass_kg * deuterium_price_per_kg

print("\n【燃料成本】")
print(f"氘價格 (估算): ${deuterium_price_per_kg}/kg")
print(f"每趟燃料成本: ${fuel_cost/1e6:.1f} 百萬")

# ============================================================
# 6. 經濟效益
# ============================================================

cargo_mass_kg = 200_000  # 200 噸貨物
price_per_kg = 500  # $500/kg
revenue = cargo_mass_kg * price_per_kg

print("\n【經濟效益（每趟）】")
print(f"貨物質量: {cargo_mass_kg/1000:.0f} 噸")
print(f"運費 (保守): ${price_per_kg}/kg")
print(f"收入: ${revenue/1e6:.1f} 百萬")
print(f"燃料成本: ${fuel_cost/1e6:.1f} 百萬")
print(f"利潤: ${(revenue - fuel_cost)/1e6:.1f} 百萬")

# ============================================================
# 7. 總結
# ============================================================
print("\n" + "="*60)
print("總結")
print("="*60)
print(f"""
✅ 核聚變飛船 Delta-V: {delta_v_kms:.2f} km/s
✅ 火星飛行時間: {mars_travel_time_days:.0f} 天（化學火箭 180-270 天）
✅ 燃料成本極低: ${fuel_cost/1e6:.1f} 百萬/趟
✅ 經濟效益: 每趟利潤 ${(revenue - fuel_cost)/1e6:.1f} 百萬

核聚變飛船性能遠超化學火箭，經濟可行！
""")
