"""
=========================================================
QORA AI
realtime.py

Real-Time Dashboard Engine

Provides live dashboard updates,
automatic refresh and data monitoring.

=========================================================
"""

import time
from datetime import datetime


class RealtimeEngine:

    def __init__(self, analytics=None):

        self.analytics = analytics
        self.last_refresh = None
        self.refresh_count = 0
        self.auto_refresh = False

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self):

        self.last_refresh = datetime.now()
        self.refresh_count += 1

        return {
            "status": "success",
            "message": "Dashboard refreshed successfully.",
            "time": self.last_refresh.strftime("%Y-%m-%d %H:%M:%S")
        }

    # =====================================================
    # LAST REFRESH
    # =====================================================

    def get_last_refresh(self):

        if self.last_refresh is None:
            return "Dashboard has not been refreshed yet."

        return self.last_refresh.strftime("%Y-%m-%d %H:%M:%S")

    # =====================================================
    # AUTO REFRESH
    # =====================================================

    def enable_auto_refresh(self):

        self.auto_refresh = True

        return "Auto refresh enabled."

    def disable_auto_refresh(self):

        self.auto_refresh = False

        return "Auto refresh disabled."

    def auto_refresh_status(self):

        return self.auto_refresh

    # =====================================================
    # REFRESH COUNT
    # =====================================================

    def total_refreshes(self):

        return self.refresh_count

    # =====================================================
    # CURRENT DASHBOARD STATUS
    # =====================================================

    def dashboard_status(self):

        return {

            "Last Refresh": self.get_last_refresh(),

            "Refresh Count": self.refresh_count,

            "Auto Refresh": self.auto_refresh

        }
    
        # =====================================================
    # LIVE KPI MONITOR
    # =====================================================

    def live_kpis(self):

        if self.analytics is None:
            return None

        return {

            "Total Orders": self.analytics.total_orders(),

            "Revenue": self.analytics.total_revenue(),

            "Shipping Cost": self.analytics.total_shipping_cost(),

            "Penalty Cost": self.analytics.total_penalty(),

            "Average Fill Rate": self.analytics.average_fill_rate(),

            "Average Carbon": self.analytics.average_carbon(),

            "Best Warehouse": self.analytics.best_warehouse(),

            "Best Plant": self.analytics.best_plant(),

            "Top Product": self.analytics.top_product()

        }

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    def health_check(self):

        if self.analytics is None:

            return {
                "status": "warning",
                "message": "Analytics engine not connected."
            }

        return {
            "status": "healthy",
            "message": "Dashboard is operating normally."
        }

    # =====================================================
    # LIVE ALERTS
    # =====================================================

    def alerts(self):

        alerts = []

        if self.analytics is None:
            return alerts

        fill = self.analytics.average_fill_rate()

        if fill is not None and fill < 90:
            alerts.append(
                "⚠ Low Fill Rate detected."
            )

        penalty = self.analytics.total_penalty()

        if penalty is not None and penalty > 10000:
            alerts.append(
                "⚠ High penalty cost detected."
            )

        warehouse = self.analytics.highest_utilization()

        if warehouse is not None:
            alerts.append(
                f"ℹ Highest utilization: {warehouse}"
            )

        carbon = self.analytics.highest_carbon()

        if carbon is not None:
            alerts.append(
                f"ℹ Highest carbon emissions: {carbon}"
            )

        return alerts

    # =====================================================
    # LIVE SUMMARY
    # =====================================================

    def live_summary(self):

        if self.analytics is None:
            return "Analytics engine unavailable."

        return f"""
Dashboard Summary

Orders: {self.analytics.total_orders()}

Revenue: {self.analytics.total_revenue()}

Fill Rate: {self.analytics.average_fill_rate()}

Shipping Cost: {self.analytics.total_shipping_cost()}

Penalty Cost: {self.analytics.total_penalty()}

Best Warehouse: {self.analytics.best_warehouse()}

Best Plant: {self.analytics.best_plant()}
"""

    # =====================================================
    # DATA CHANGE DETECTOR
    # =====================================================

    def data_changed(self, previous_rows, current_rows):

        return previous_rows != current_rows

    # =====================================================
    # WAIT FOR REFRESH
    # =====================================================

    def wait(self, seconds=5):

        time.sleep(seconds)

        return self.refresh()
    
        # =====================================================
    # CONTINUOUS MONITOR
    # =====================================================

    def monitor(self):

        return {
            "status": "Running",
            "last_refresh": self.get_last_refresh(),
            "refresh_count": self.refresh_count,
            "auto_refresh": self.auto_refresh,
            "health": self.health_check()
        }

    # =====================================================
    # PERFORMANCE STATISTICS
    # =====================================================

    def performance_statistics(self):

        stats = {
            "Refresh Count": self.refresh_count,
            "Auto Refresh": self.auto_refresh,
            "Last Refresh": self.get_last_refresh()
        }

        if self.analytics is not None:

            stats["Total Orders"] = self.analytics.total_orders()
            stats["Revenue"] = self.analytics.total_revenue()
            stats["Fill Rate"] = self.analytics.average_fill_rate()
            stats["Shipping Cost"] = self.analytics.total_shipping_cost()
            stats["Penalty Cost"] = self.analytics.total_penalty()

        return stats

    # =====================================================
    # REFRESH HISTORY
    # =====================================================

    def refresh_report(self):

        return f"""
REALTIME DASHBOARD REPORT

Last Refresh:
{self.get_last_refresh()}

Refresh Count:
{self.refresh_count}

Auto Refresh:
{self.auto_refresh}
"""

    # =====================================================
    # SESSION INFO
    # =====================================================

    def session_info(self):

        return {
            "Engine": "Qora AI Realtime Engine",
            "Connected": self.analytics is not None,
            "Auto Refresh": self.auto_refresh,
            "Refreshes": self.refresh_count
        }

    # =====================================================
    # COMPLETE STATUS
    # =====================================================

    def status(self):

        return {
            "dashboard": self.dashboard_status(),
            "health": self.health_check(),
            "alerts": self.alerts(),
            "statistics": self.performance_statistics(),
            "session": self.session_info()
        }

    # =====================================================
    # EXPORT STATUS
    # =====================================================

    def export(self):

        return {
            "status": self.status(),
            "summary": self.live_summary(),
            "kpis": self.live_kpis(),
            "alerts": self.alerts()
        }

    # =====================================================
    # RESET REALTIME ENGINE
    # =====================================================

    def reset(self):

        self.last_refresh = None
        self.refresh_count = 0
        self.auto_refresh = False

        return "Realtime engine has been reset."

# =====================================================
# END OF FILE
# =====================================================