from flask import Flask, render_template, request, redirect, url_for, flash
from database.db import init_db, get_db_connection
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'slickdesk-secret-key'

@app.route('/')
def index():
    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)

@app.route('/submit', methods=['GET', 'POST'])
def submit_ticket():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        category = request.form['category']
        priority = request.form['priority']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO tickets (name, email, category, priority, description, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (name, email, category, priority, description, 'Open', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
        conn.commit()
        conn.close()

        flash(f'Ticket submitted successfully! We will contact you at {email}.', 'success')
        return redirect(url_for('index'))

    return render_template('submit.html')

@app.route('/ticket/<int:ticket_id>')
def view_ticket(ticket_id):
    conn = get_db_connection()
    ticket = conn.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()
    conn.close()
    return render_template('ticket.html', ticket=ticket)

@app.route('/ticket/<int:ticket_id>/update', methods=['POST'])
def update_ticket(ticket_id):
    status = request.form['status']
    conn = get_db_connection()
    conn.execute('UPDATE tickets SET status = ? WHERE id = ?', (status, ticket_id))
    conn.commit()
    conn.close()
    flash('Ticket status updated!', 'success')
    return redirect(url_for('view_ticket', ticket_id=ticket_id))

@app.route('/assets')
def assets():
    conn = get_db_connection()
    assets = conn.execute('SELECT * FROM assets ORDER BY name').fetchall()
    conn.close()
    return render_template('assets.html', assets=assets)

@app.route('/assets/add', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        name = request.form['name']
        asset_type = request.form['asset_type']
        serial = request.form['serial']
        assigned_to = request.form['assigned_to']
        status = request.form['status']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO assets (name, asset_type, serial, assigned_to, status) VALUES (?, ?, ?, ?, ?)',
            (name, asset_type, serial, assigned_to, status)
        )
        conn.commit()
        conn.close()
        flash('Asset added successfully!', 'success')
        return redirect(url_for('assets'))

    return render_template('add_asset.html')

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    total = conn.execute('SELECT COUNT(*) FROM tickets').fetchone()[0]
    open_tickets = conn.execute("SELECT COUNT(*) FROM tickets WHERE status = 'Open'").fetchone()[0]
    resolved = conn.execute("SELECT COUNT(*) FROM tickets WHERE status = 'Resolved'").fetchone()[0]
    total_assets = conn.execute('SELECT COUNT(*) FROM assets').fetchone()[0]
    conn.close()
    return render_template('dashboard.html', total=total, open_tickets=open_tickets, resolved=resolved, total_assets=total_assets)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
