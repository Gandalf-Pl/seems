# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import psycopg2
import xlsxwriter

connection = psycopg2.connect(
    host='192.168.1.4',
    port='5432',
    user='***',
    password="****",
    database='*****'
)

def get_shanghai_restaurant_data():
    raw_sql = """SELECT restaurant_restaurant.id, restaurant_restaurant.name_zh
                FROM restaurant_restaurant
                    INNER JOIN restaurant_cityarea ON restaurant_cityarea.id = restaurant_restaurant.city_area_id
                    INNER JOIN restaurant_city ON restaurant_city.id = restaurant_cityarea.city_id
                WHERE restaurant_city.name_zh = '上海';
            """
    cursor = connection.cursor()
    cursor.execute(raw_sql)
    restaurant_data = cursor.fetchall()
    cursor.close()
    return restaurant_data


def get_shanghai_is_authenticated_restaurant_info():
    raw_sql = """
    SELECT restaurant_restaurant.id, sum(cart_order.activity_subsidy_total) AS total_subsidy, count(*) as num
    FROM restaurant_restaurant
    INNER JOIN restaurant_cityarea ON restaurant_cityarea.id = restaurant_restaurant.city_area_id
    INNER JOIN restaurant_city ON restaurant_city.id = restaurant_cityarea.city_id
    LEFT JOIN cart_order ON restaurant_restaurant.id = cart_order.restaurant_id
    WHERE restaurant_city.name_zh = '上海' AND cart_order.created_at >= '2015-10-22'
    AND cart_order.created_at < '2015-10-29' AND restaurant_restaurant.is_authenticated is True GROUP BY restaurant_restaurant.id ORDER BY num;
    """
    cursor = connection.cursor()
    cursor.execute(raw_sql)
    authenticated_restaurant_data = cursor.fetchall()
    cursor.close()
    return authenticated_restaurant_data


def get_shanghai_authenticated_activity_restaruant_info():
    raw_sql = """
    SELECT restaurant_restaurant.id, sum(cart_order.activity_subsidy_total) AS total_subsidy, count(*) as num
    FROM restaurant_restaurant
    INNER JOIN restaurant_cityarea ON restaurant_cityarea.id = restaurant_restaurant.city_area_id
    INNER JOIN restaurant_city ON restaurant_city.id = restaurant_cityarea.city_id
    INNER JOIN restaurant_relatedactivityrestaurant ON restaurant_relatedactivityrestaurant.restaurant_id = restaurant_restaurant.id
    LEFT JOIN cart_order ON restaurant_restaurant.id = cart_order.restaurant_id
    WHERE restaurant_city.name_zh = '上海' AND cart_order.created_at >= '2015-10-22'
    AND cart_order.created_at < '2015-10-29' AND restaurant_relatedactivityrestaurant.activity_id=42 GROUP BY restaurant_restaurant.id ORDER BY num;
    """
    cursor = connection.cursor()
    cursor.execute(raw_sql)
    activity_restaurant_data = cursor.fetchall()
    cursor.close()
    return activity_restaurant_data


def export_report():
    """"""
    restaurant_data_dict = dict()
    restaurant_data = get_shanghai_restaurant_data()
    authenticated_restaurant_data = get_shanghai_is_authenticated_restaurant_info()
    activity_restaurant_data = get_shanghai_authenticated_activity_restaruant_info()

    print len(restaurant_data)
    for restaurant in restaurant_data:
        restaurant_id = restaurant[0]
        restaurant_data_dict.update({
            restaurant_id: {
                "restaurant_id": restaurant[0],
                "restaurant_name": restaurant[1],
                "total_subsidy": 0,
                "order_count": 0,
                "is_authenticated": 0,
                "activity_restaurant": 0,
            }
        })
    print len(activity_restaurant_data)
    for item in activity_restaurant_data:
        if item[0] not in restaurant_data_dict:
            print "repeat in activity_restaurant_data", item[0]
            continue
        restaurant_data_dict[item[0]].update({"total_subsidy": item[1], "order_count": item[2], "activity_restaurant": 1})

    print len(authenticated_restaurant_data)
    for r_data in authenticated_restaurant_data:
        if r_data[0] not in restaurant_data_dict:
            print "repeat in authenticated_restaurant_data", r_data[0]
            continue
        restaurant_data_dict[r_data[0]].update({"total_subsidy": r_data[1], "order_count": r_data[2], "is_authenticated": 1})

    headers = ("餐厅id", "餐厅名称", "补贴金额", "订单总数", "认证餐厅", "蓝标餐厅")

    wb = xlsxwriter.Workbook("/home/panlei/export.xlsx")
    restaurant_info = wb.add_worksheet("餐厅信息")
    for num, column in enumerate(headers):
        restaurant_info.write(0, num, column)

    for row, r_id in enumerate(restaurant_data_dict):
        info = restaurant_data_dict[r_id]
        data = [info["restaurant_id"], info["restaurant_name"].decode("utf8"), info["total_subsidy"], info["order_count"], info["is_authenticated"], info["activity_restaurant"]]
        row += 1
        col = 0
        for d in data:
            restaurant_info.write(row, col, d)
            col +=1
    wb.close()
    print "export over"

if __name__ == "__main__":
    export_report()
